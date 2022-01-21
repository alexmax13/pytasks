# p - position
# 2p - left child 2p + 1 right child
from typing import List


class BinHeap:

    def __init__(self) -> None:
        self.heap_list: List[int] = [0]
        self.current_size: int = 0

    def perc_up(self, i) -> None:
        while i // 2 > 0:
            if self.heap_list[i] > self.heap_list[i // 2]:
                self.heap_list[i // 2], self.heap_list[i] = self.heap_list[i], self.heap_list[i // 2]
            i //= 2

    def perc_down(self, i) -> None:
        while (i * 2) <= self.current_size:
            mc = self.max_child(i)
            if self.heap_list[i] < self.heap_list[mc]:
                self.heap_list[i], self.heap_list[mc] = self.heap_list[mc], self.heap_list[i]
            i = mc

    def max_child(self, i) -> int:
        if i * 2 + 1 > self.current_size:
            return i * 2
        if self.heap_list[i * 2] > self.heap_list[i * 2 + 1]:
            return i * 2
        else:
            return i * 2 + 1

    def del_min(self) -> int:
        ret_val = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size -= 1
        self.heap_list.pop()
        self.perc_down(1)
        return ret_val

    def Print(self):

        for i in range(1, (self.current_size // 2) + 1):
            buffer = " PARENT : " + str(self.heap_list[i])
            if 2 * i < len(self.heap_list):
                buffer += " LEFT CHILD : " + str(self.heap_list[2 * i])
            if 2 * i + 1 < len(self.heap_list):
                buffer += " RIGHT CHILD : " + str(self.heap_list[2 * i + 1])
            print(buffer)

    def build_heap(self, items: List[int]) -> None:
        i = len(items) // 2
        self.current_size = len(items)
        self.heap_list = [0] + items[:]
        while i > 0:
            self.perc_down(i)
            i -= 1

    def insert(self, k) -> None:
        self.heap_list.append(k)
        self.current_size += 1
        self.perc_up(self.current_size)


if __name__ == "__main__":
    kucha = BinHeap()
    list_1 = [5, 8, 3, 20, 145, 98, 4, 2]
    kucha.build_heap(list_1)
    kucha.Print()
