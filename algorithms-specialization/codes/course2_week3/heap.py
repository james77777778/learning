from typing import List, Tuple, Any


class Heap:
    def __init__(self):
        self.data: List[Tuple[int, Any]] = [(0, 0)]  # 1 dummy

    def _get_parent_idx(self, idx: int):
        return idx // 2

    def _get_child_idxs(self, idx: int):
        return (idx * 2, idx * 2 + 1)

    def _bubble_up(self):
        raise NotImplementedError()

    def _bubble_down(self):
        raise NotImplementedError()

    @property
    def length(self):
        return len(self.data) - 1

    def insert(self, key: int, value):
        # insert to the last
        self.data.append((key, value))
        # bubble-up
        self._bubble_up()

    def peek(self):
        assert self.length > 0, 'Heap is empty'

        return self.data[1]

    def get_all_keys(self):
        keys = [data[0] for data in self.data]
        keys = keys[1:]
        return keys


class MinHeap(Heap):
    def _bubble_up(self):
        child_idx = self.length
        while child_idx > 1:
            parent_idx = self._get_parent_idx(child_idx)
            child_key = self.data[child_idx][0]
            parent_key = self.data[parent_idx][0]
            if child_key < parent_key:
                # swap
                # print(f'Swap! child: {child_idx} {child_key}, parent: {parent_idx} {parent_key}')
                self.data[child_idx], self.data[parent_idx] = self.data[parent_idx], self.data[child_idx]
            else:
                break
            child_idx = parent_idx

    def _bubble_down(self):
        parent_idx = 1
        while parent_idx <= self.length:
            child1_idx, child2_idx = self._get_child_idxs(parent_idx)
            if child1_idx >= self.length:
                break
            elif child2_idx > self.length:
                child1_key = self.data[child1_idx][0]
                child_idx, child_key = child1_idx, child1_key
            else:
                child1_key = self.data[child1_idx][0]
                child2_key = self.data[child2_idx][0]
                child_idx, child_key = (child1_idx, child1_key) if child1_key < child2_key else (child2_idx, child2_key)

            parent_key = self.data[parent_idx][0]
            if parent_key > child_key:
                self.data[child_idx], self.data[parent_idx] = self.data[parent_idx], self.data[child_idx]
            else:
                break
            parent_idx = child_idx

    def extract_min(self):
        self.data[1], self.data[-1] = self.data[-1], self.data[1]
        res = self.data.pop()
        self._bubble_down()
        return res


class MaxHeap(Heap):
    def _bubble_up(self):
        child_idx = self.length
        while child_idx > 1:
            parent_idx = self._get_parent_idx(child_idx)
            child_key = self.data[child_idx][0]
            parent_key = self.data[parent_idx][0]
            if child_key > parent_key:
                # swap
                # print(f'Swap! child: {child_idx} {child_key}, parent: {parent_idx} {parent_key}')
                self.data[child_idx], self.data[parent_idx] = self.data[parent_idx], self.data[child_idx]
            else:
                break
            child_idx = parent_idx

    def _bubble_down(self):
        parent_idx = 1
        while parent_idx <= self.length:
            child1_idx, child2_idx = self._get_child_idxs(parent_idx)
            if child1_idx >= self.length:
                break
            elif child2_idx > self.length:
                child1_key = self.data[child1_idx][0]
                child_idx, child_key = child1_idx, child1_key
            else:
                child1_key = self.data[child1_idx][0]
                child2_key = self.data[child2_idx][0]
                child_idx, child_key = (child1_idx, child1_key) if child1_key > child2_key else (child2_idx, child2_key)

            parent_key = self.data[parent_idx][0]
            if parent_key < child_key:
                self.data[child_idx], self.data[parent_idx] = self.data[parent_idx], self.data[child_idx]
            else:
                break
            parent_idx = child_idx

    def extract_max(self):
        self.data[1], self.data[-1] = self.data[-1], self.data[1]
        res = self.data.pop()
        self._bubble_down()
        return res


if __name__ == '__main__':
    min_heap = MinHeap()
    min_heap.data = [(0, 0), (4, 4), (4, 4), (8, 8), (9, 9), (4, 4), (12, 12), (9, 9), (11, 11), (13, 13)]
    min_heap.insert(7, 7)
    min_heap.insert(10, 10)
    min_heap.insert(5, 5)
    print(min_heap.get_all_keys())

    min_heap.data = [(0, 0), (4, 4), (4, 4), (8, 8), (9, 9), (4, 4), (12, 12), (9, 9), (11, 11), (13, 13)]
    data = min_heap.extract_min()
    print(min_heap.get_all_keys())
