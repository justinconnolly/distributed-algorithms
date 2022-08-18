class Network:
    class Node:
        def __init__(self, id: int):
            self.id = id
            self.neighbours = {}    # list of Nodes

        def info(self):
            print(f"Node: {self.id}")

        def other_info(self, other_node_info):
            print(f"My id: {self.id}, calling: ")
            other_node_info()

        def add_edge(self, node, weight):
            # self.neighbours.append([node, weight])
            self.neighbours[node] = weight

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
    
    def __init__(self, num_nodes):
        self.nodes = [self.Node(x) for x in range(num_nodes)]
    
    def get_node(self, id):
        return self.nodes[id]

    def print_nodes(self):
        for node in self.nodes:
            node.print_neighbours()

    def add_edge(self, node1, node2, weight):
        # self.get_node(node1).add_edge(self.get_node(node2), weight)
        # self.get_node(node2).add_edge(self.get_node(node1), weight)
        self.get_node(node1).add_edge(node2, weight)
        self.get_node(node2).add_edge(node1, weight)

    def print_path(self, end, path_dict):
        path = [end]
        curr = path_dict[end]
        while curr is not None:
            path.append(curr)
            curr = path_dict[curr]
        print(path[::-1])

    def bfs(self, start, end):
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
        # print(path)
            


if __name__ == "__main__":
    network = Network()
