from heap import MinHeap, MaxHeap


class MedianMaintenance:
    def __init__(self):
        self.min_heap = MinHeap()
        self.max_heap = MaxHeap()

    def _rebalance(self):
        if self.min_heap.length > self.max_heap.length:
            min_key, min_value = self.min_heap.extract_min()
            self.max_heap.insert(min_key, min_value)
        if self.max_heap.length > self.min_heap.length + 1:
            max_key, max_value = self.max_heap.extract_max()
            self.min_heap.insert(max_key, max_value)

    def add_data(self, key, value):
        if self.max_heap.length == 0:
            self.max_heap.insert(key, value)
            return

        max_key, _ = self.max_heap.peek()

        if key > max_key:
            self.min_heap.insert(key, value)
        else:
            self.max_heap.insert(key, value)

        self._rebalance()

    def get_median(self):
        if self.min_heap.length + self.max_heap.length == 0:
            raise ValueError
        return self.max_heap.peek()


if __name__ == '__main__':
    median_maintenance = MedianMaintenance()
    all_medians = []

    for data in [6331, 2793, 1640, 9290, 225, 625, 6195, 2303, 5685, 1354]:
        median_maintenance.add_data(data, data)
        all_medians.append(median_maintenance.get_median()[0])
    print(all_medians)
    print(sum(all_medians))

    # assignment
    median_maintenance = MedianMaintenance()
    res = 0
    with open('Median.txt', 'r') as f:
        for line in f:
            data = int(line.strip())
            median_maintenance.add_data(data, data)
            res += median_maintenance.get_median()[0]
    print(res)
    print(res % 10000)
