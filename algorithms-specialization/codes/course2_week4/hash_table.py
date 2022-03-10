from typing import Dict


class OpenAddressingHashTable:
    def __init__(self):
        self.data: Dict[int, int] = {}

    def __len__(self):
        return len(self.data)

    def insert(self, key: int):
        hash_value = hash(key)
        while hash_value in self.data and self.data[hash_value] != key:
            hash_value += 1

        self.data[hash_value] = key

    def delete(self, key: int):
        hash_value = hash(key)

        if hash_value not in self.data:
            raise KeyError(f'No key: {key}')

        while self.data[hash_value] != key:
            hash_value += 1
            if hash_value not in self.data:
                raise KeyError(f'No key: {key}')

        del self.data[hash_value]

    def lookup(self, key: int):
        hash_value = hash(key)

        if hash_value not in self.data:
            return None

        while self.data[hash_value] != key:
            hash_value += 1
            if hash_value not in self.data:
                return None

        return self.data[hash_value]

    def keys(self):
        return self.data.keys()


if __name__ == '__main__':
    hash_table = OpenAddressingHashTable()
    hash_table.insert(100)
    hash_table.insert(200)
    print(hash_table.lookup(200))
    print(hash_table.lookup(201))

    for k in hash_table.keys():
        print(k, type(k))
