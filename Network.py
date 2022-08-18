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
            self.neighbours[node.id] = weight

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
        self.get_node(node1).add_edge(self.get_node(node2), weight)
        self.get_node(node2).add_edge(self.get_node(node1), weight)


if __name__ == "__main__":
    network = Network()
