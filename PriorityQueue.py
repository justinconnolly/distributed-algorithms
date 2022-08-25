from typing import List

# contains is O(n), and decrease_key is O(n + logn). Need to fix the index dictionary to reduce those of O(1) and O(logn)
class PriorityQueue:
    def __init__(self) -> None:
        self.a = []
        self.d = {}
    
    def get_parent(self, i: int) -> int:
        return (i - 1) // 2
    
    def get_left(self, i: int) -> int:
        return (i * 2) + 1

    def get_right(self, i: int) -> int:
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
            self.d[self.a[0][1]] = 0
            self.trickle_down(0)
        else:
            val = self.a.pop()
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
        # for index, pair in enumerate(self.a):
        #     if pair[1] == node:
        #         i = index
        #         break
        
        self.a[i][0] = weight
        self.bubble_up(i)

    def contains(self, node: int) -> bool:
        return node in self.d
        for i, pair in enumerate(self.a):
            if pair[1] == node:
                return True
        return False

    def is_empty(self):
        return len(self.a) == 0

    def get_weight(self, id):
        for val in self.a:
            if val[1] == id:
                return val[0]
        return -1


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
        pq.add(item[0], item[1])
        print(pq.a)
    pq.decrease_key(2,0)
    print(pq.a)
    print(pq.d)
    for i in arr:
        print(pq.get_min())
        print(pq.a)