# TODO: Rewrite the algorithm!!

from timeit import default_timer as timer

# computing simple numbers
hamm = [0] * 300
k = 0
for i in range(24):
    for j in range(i, 24):
        mask = 1 << i
        mask2 = 1 << j
        hamm[k] = mask | mask2
        k = k + 1


# function that computes neighbors for the given point
def neighbors(x):
    result = []
    for i in hamm:
        if points[x ^ i] != 0:
            result.append(x ^ i)
    return result


# reading the data into arrays points and index
points = [0] * pow(2, 24)
index = []

start = timer()

with open("clustering_big.txt") as f:
    next(f)
    cluster = 1
    for line in f:
        curindex = int(line.replace(' ', ''), base=2)
        index.append(curindex)
        points[curindex] = cluster
        cluster = cluster + 1

readend = timer()
print("reading data:", readend - start)

# performing clustering
names = [0]
loopstart = timer()
for i in index:
    if points[i] in names:
        continue
    nclust = [i]
    while len(nclust) != 0:
        nnclust = []
        for dot in nclust:
            for ind in neighbors(dot):
                if points[ind] != points[i]:
                    nnclust.append(ind)
                    points[ind] = points[i]
        nclust = nnclust
    names.append(points[i])
end = timer()
print("loop time", end - loopstart)
print("total time", end - start)
print(len(names) - 1)
