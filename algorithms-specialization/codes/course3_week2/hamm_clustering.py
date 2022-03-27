def parse_points(path: str):
    points = {}
    with open(path) as f:
        next(f)
        for i, line in enumerate(f):
            curindex = int(line.replace(' ', ''), base=2)  # 24 bit representation to int number
            points[curindex] = i
    return points


def compute_hamm():
    # computing simple numbers
    # a XOR b = c implies a XOR c = b
    # a: the 24 bit query
    # c: the xor_mask that has 2 ones in 24 bit
    # b: the neighbor of a
    hamm = []
    for i in range(24):
        for j in range(i, 24):
            mask1 = 1 << i
            mask2 = 1 << j
            xor_mask = mask1 | mask2
            hamm.append(xor_mask)
    return hamm


# function that computes neighbors for the given point
def neighbors(x, hamm):
    result = []
    for i in hamm:
        if x ^ i in points:
            result.append(x ^ i)
    return result


def clustering(points, hamm):
    # performing clustering
    clusters = []
    for i in points.keys():
        if points[i] in clusters:
            continue
        nclust = [i]
        while len(nclust) != 0:
            nnclust = []
            for dot in nclust:
                for ind in neighbors(dot, hamm):
                    if points[ind] != points[i]:
                        nnclust.append(ind)
                        points[ind] = points[i]
            nclust = nnclust
        clusters.append(points[i])
    return clusters


if __name__ == '__main__':
    points = parse_points('clustering_big.txt')
    hamm = compute_hamm()
    clusters = clustering(points, hamm)
    print(f'The number of clusters: {len(clusters)}')
