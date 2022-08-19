from typing import List
class PriorityQueue:
    def __init__(self) -> None:
        self.a = []
        self.d = {}
    
    def get_parent(self, i: int) -> None:
        return i // 2
    
    def get_left(self, i: int) -> None:
        return (i * 2) + 1

    def get_right(self, i: int) -> None:
        return 2 * (i + 1)

    def add(self, x, weight) -> None:
        self.a.append([weight, x])
        self.d[x] = len(self.a) - 1
        self.bubble_up(len(self.a) - 1)

    def bubble_up(self, i: int) -> None:
        p = self.get_parent(i)
        while i > 0 and self.a[i] < self.a[p]:
            self.a[i], self.a[p] = self.a[p], self.a[i]
            self.d[self.a[i][1]], self.d[self.a[p][1]] = self.d[self.a[p][1]], self.d[self.a[i][1]]
            i = p
            p = self.get_parent(i)

    def get_min(self) -> List[int]:
        x = self.a[0]
        del self.d[x[1]]
        if len(self.a) > 1:
            self.a[0] = self.a.pop()
            self.trickle_down(0)
        else:
            self.a.pop()
        return x

    def trickle_down(self, i: int) -> None:
        while i >= 0:
            j = -1
            r = self.get_right(i)
            if r < len(self.a) and self.a[r] < self.a[i]:
                l = self.get_left(i)
                if self.a[l] < self.a[r]:
                    j = l
                else:
                    j = r
            else:
                l = self.get_left(i)
                if l < len(self.a) and self.a[l] < self.a[i]:
                    j = l
            if j >= 0:
                self.a[j], self.a[i] = self.a[i], self.a[j]
                self.d[self.a[j][1]], self.d[self.a[i][1]] = self.d[self.a[i][1]], self.d[self.a[j][1]]
            i = j

    def decrease_key(self, node: int, weight: int) -> None:
        i = self.d[node]
        self.a[i][0] = weight
        self.bubble_up(i)

    def contains(self, node: int) -> bool:
        return node in self.d

    def is_empty(self):
        return len(self.a) == 0


if __name__ == "__main__":
    arr = [
        [1,4],
        [5,1],
        [3,0],
        [6,2],
        [2,10]
        ]
    pq = PriorityQueue()

    for item in arr:
        pq.add(item)
        print(pq.a)
    pq.decrease_key(2,0)
    print(pq.a)
    print(pq.d)
    for i in arr:
        print(pq.get_min())
        print(pq.a)