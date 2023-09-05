"""
用列表实现一个数组
"""


class Array:
    def __init__(self, size: int):
        self._data = []
        self.size = size

    def __len__(self) -> int:
        return len(self._data)

    def __iter__(self):
        for item in self._data:
            yield item

    def find(self, index: int):
        try:
            return self._data[index]
        except IndexError:
            return None

    def delete(self, index):
        try:
            self._data.pop(index)
            return True
        except IndexError:
            return False

    def insert(self, index: int, value: int):
        if len(self) >= self.size:
            return False
        self._data.insert(index, value)

    def print_all(self):
        for item in self:
            print(item)


if __name__ == "__main__":
    array = Array(5)
    array.insert(0, 3)
    array.insert(0, 4)
    array.insert(1, 5)
    array.insert(3, 9)
    array.insert(3, 10)
    assert array.insert(0, 100) is False
    assert len(array) == 5
    assert array.find(1) == 5
    assert array.delete(4) is True
    array.print_all()