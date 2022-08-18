class Network:
    class Node:
        def __init__(self, id: int):
            self.id = id
            self.neighbours = {}    # dictionary of k:v id:weight

        def info(self):
            print(f"Node: {self.id}")

        def other_info(self, other_node_info):
            print(f"My id: {self.id}, calling: ")
            other_node_info()

        def add_edge(self, id, weight):
            self.neighbours[id] = weight

        def get_unweighted_neighbours(self):
            return [neighbour for neighbour in self.neighbours]

        def print_neighbours(self):
            print("-----------------------")
            self.info()
            print("Neighbours:")
            for neighbour in self.neighbours:
                # print(", ".join([str(x) for x in self.neighbours]))
                print(f"ID: {neighbour}, weight: {self.neighbours[neighbour]}")
            print("-----------------------")

        def get_weight(self, id):
            return self.neighbours[id]
    
    def __init__(self, num_nodes):
        self.nodes = [self.Node(x) for x in range(num_nodes)]
    
    def get_node(self, id):
        if id >= len(self.nodes) or id < 0:
            return -1
        return self.nodes[id]

    def print_nodes(self):
        for node in self.nodes:
            node.print_neighbours()

    def add_edge(self, node1, node2, weight):
        # self.get_node(node1).add_edge(self.get_node(node2), weight)
        # self.get_node(node2).add_edge(self.get_node(node1), weight)
        self.get_node(node1).add_edge(node2, weight)
        self.get_node(node2).add_edge(node1, weight)


    def get_path_weight(self, path):
        total_weight = 0
        for i in range(1, len(path)):
            total_weight += self.get_node(path[i]).get_weight(path[i - 1])
        return total_weight

    def print_path(self, end, path_dict):
        path = [end]
        curr = path_dict[end]
        while curr is not None:
            path.append(curr)
            curr = path_dict[curr]
        print(f"{path[::-1 ]}, Weight: {self.get_path_weight(path)}")

    def bfs(self, start, end):
        if self.get_node(start) == -1 or self.get_node(end) == -1:
            if self.get_node(start) == -1 and self.get_node(end) == -1:
                print("Neither nodes exist.")
            elif self.get_node(start) == -1:
                print("Start node does not exist.")
            else:
                print("End node does not exist.")
            return
        print(f"Beginning BFS from {start} to {end}")
        queue = [start]
        seen = set()
        seen.add(start)
        path = {}
        path[start] = None
        while queue:
            curr = queue.pop(0)
            for neighbour in self.get_node(curr).get_unweighted_neighbours():
                if neighbour not in seen:
                    path[neighbour] = curr
                    if neighbour == end:
                        print(f"Reached {end}")
                        self.print_path(end, path)
                        return
                    seen.add(neighbour)
                    queue.append(neighbour)
        print("Unreachable.")

    # why not, right? provide BFS = True parameter otherwise it'll DFS
    def first_search(self, start, end, BFS=False):
        if self.get_node(start) == -1 or self.get_node(end) == -1:
            if self.get_node(start) == -1 and self.get_node(end) == -1:
                print("Neither nodes exist.")
            elif self.get_node(start) == -1:
                print("Start node does not exist.")
            else:
                print("End node does not exist.")
            return
        print(f"Beginning {'BFS' if BFS else 'DFS'} from {start} to {end}")
        queue = [start]
        seen = set()
        seen.add(start)
        path = {}
        path[start] = None
        while queue:
            curr = queue.pop(0) if BFS else queue.pop()
            for neighbour in self.get_node(curr).get_unweighted_neighbours():
                if neighbour not in seen:
                    path[neighbour] = curr
                    if neighbour == end:
                        print(f"Reached {end}")
                        self.print_path(end, path)
                        return
                    seen.add(neighbour)
                    queue.append(neighbour)
        print("Unreachable.")
            


if __name__ == "__main__":
    network = Network()
