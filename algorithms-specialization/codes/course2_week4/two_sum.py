import multiprocessing as mp

from tqdm import tqdm

from hash_table import OpenAddressingHashTable


def two_sum_count(hash_table: OpenAddressingHashTable, min=-10000, max=10001) -> int:
    res = OpenAddressingHashTable()
    keys = hash_table.keys()

    for x in keys:
        for t in range(min, max):
            y = t - x
            if x != y and hash_table.lookup(y):
                res.insert(t)

    print(f'min: {min}, max: {max}, result: {len(res)}')
    return len(res)


if __name__ == '__main__':
    hash_table = OpenAddressingHashTable()
    hash_table.insert(10)
    hash_table.insert(20)
    count = two_sum_count(hash_table)
    print(f'Count: {count}')

    hash_table = OpenAddressingHashTable()
    with open('algo1-programming_prob-2sum.txt', 'r') as f:
        for line in f:
            number = int(line.strip())
            hash_table.insert(number)
    print(f'Total distinct number of dataset: {len(hash_table)}')

    step_size = 100
    chunk_args = [(hash_table, start, start + step_size) for start in range(-10000, 10001, step_size)]
    chunk_args[-1] = (hash_table, chunk_args[-1][1], 10001)
    print(len(chunk_args))

    with mp.Pool(8) as pool:
        results = pool.starmap(two_sum_count, tqdm(chunk_args), chunksize=1)
    count = sum(results)
    print(f'Count: {count}')
