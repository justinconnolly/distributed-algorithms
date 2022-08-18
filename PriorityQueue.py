
class PriorityQueue:
    def __init__(self) -> None:
        self.a = []
        self.d = {}
    
    def get_parent(self, i):
        return i // 2
    
    def get_left(self, i):
        return (i * 2)

    def get_right(self, i):
        return 2 * (i + 1)

    def add(self, x):
        self.a.append(x)
        self.d[x[1]] = len(self.a) - 1
        self.bubble_up(len(self.a) - 1)

    def bubble_up(self, i):
        p = self.get_parent(i)
        while i > 0 and self.a[i] < self.a[p]:
            self.a[i], self.a[p] = self.a[p], self.a[i]
            self.d[self.a[i][1]], self.d[self.a[p][1]] = self.d[self.a[p][1]], self.d[self.a[i][1]]
            i = p
            p = self.get_parent(i)

    def get_min(self):
        x = self.a[0]
        del self.d[x[1]]
        self.a[0] = self.a.pop()
        self.trickle_down(0)
        return x

    def trickle_down(self, i):
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

    def decrease_key(self, item, key):
        i = self.d[item]
        self.a[i][0] = key
        self.bubble_up(i)

if __name__ == "__main__":
    arr = [
        [1,4],
        [5,1],
        [3,0],
        [5,2],
        [2,10]
        ]
    pq = PriorityQueue()

    for item in arr:
        pq.add(item)

    print(pq.a)

    pq.a[2][0] = 0
    pq.bubble_up(2)
    print(pq.a)
    print(pq.d)