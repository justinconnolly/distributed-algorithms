import math
from typing import List, Callable
from PriorityQueue import PriorityQueue

class Graph:
    class Node:
        def __init__(self, id: int) -> None:
            self.id = id
            self.neighbours = {}    # dictionary of k:v id:weight

        def info(self) -> None:
            print(f"Node: {self.id}")

        def other_info(self, other_node_info: Callable) -> None:
            print(f"My id: {self.id}, calling: ")
            other_node_info()

        def add_edge(self, id: int, weight: int) -> None:
            self.neighbours[id] = weight

        def get_unweighted_neighbours(self) -> List[int]:
            return [neighbour for neighbour in self.neighbours]

        def get_weighted_neighours(self) -> dict:
            return self.neighbours

        def print_neighbours(self) -> None:
            print("-----------------------")
            self.info()
            print("Neighbours:")
            for neighbour in self.neighbours:
                print(f"ID: {neighbour}, weight: {self.neighbours[neighbour]}")
            print("-----------------------")

        def get_weight(self, id) -> int:
            return self.neighbours[id]
    
    def __init__(self, num_nodes: int) -> None:
        self.nodes = [self.Node(x) for x in range(num_nodes)]
    
    def get_node(self, id: int) -> Node:
        if id >= len(self.nodes) or id < 0:
            return -1
        return self.nodes[id]

    def print_nodes(self) -> None:
        for node in self.nodes:
            node.print_neighbours()

    # def add_edge(self, node1, node2, weight):
    def add_edge(self, new_edge: List[int]) -> None:
        node1, node2, weight = new_edge
        # self.get_node(node1).add_edge(self.get_node(node2), weight)
        # self.get_node(node2).add_edge(self.get_node(node1), weight)
        self.get_node(node1).add_edge(node2, weight)
        self.get_node(node2).add_edge(node1, weight)
    
    # not strictly necessary, but reasonable to have
    def update_edge(self, updated_edge: List[int]) -> None:
        self.add_edge(updated_edge)


    def get_path_weight(self, path: List[List[int]]) -> int:
        total_weight = 0
        for i in range(1, len(path)):
            total_weight += self.get_node(path[i]).get_weight(path[i - 1])
        return total_weight

    def print_path(self, end: int, path_dict: dict) -> List[int]:
        path = [end]
        curr = path_dict[end]
        while curr is not None:
            path.append(curr)
            curr = path_dict[curr]
        print(f"{path[::-1 ]}, Weight: {self.get_path_weight(path)}")
        return path[::-1]

    # this was made redundant with the addition of first_search below
    def bfs(self, start: int, end: int) -> None:
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

    def check_nodes_exist(self, node1, node2):
        if self.get_node(node1) == -1 or self.get_node(node2) == -1:
            if self.get_node(node1) == -1 and self.get_node(node2) == -1:
                print("Neither nodes exist.")
            elif self.get_node(node1) == -1:
                print("Start node does not exist.")
            else:
                print("End node does not exist.")
            return False
        return True

    # why not, right? provide BFS = True parameter otherwise it'll DFS. Could probably return the path?
    def first_search(self, start: int, end: int, BFS: bool=False) -> None:
        if not self.check_nodes_exist(start, end):
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
                        return(self.print_path(end, path))
                        return path
                    seen.add(neighbour)
                    queue.append(neighbour)
        print("Unreachable.")

    def get_path_matrix(self) -> List[List[int]]:
        paths = [[math.inf for x in range(len(self.nodes))] for y in range(len(self.nodes))]
        for i,node in enumerate(self.nodes):
            paths[i][i] = 0
            for key in node.get_weighted_neighours():
                paths[i][key] = node.get_weight(key)
        return paths

    def floyd_warshall(self) -> List[List[int]]:
        paths = self.get_path_matrix()
        for k in range(len(paths)):
            for j in range(len(paths)):
                for i in range(len(paths)):
                    paths[i][j] = min([paths[i][k] + paths[k][j], paths[i][j]])
        return paths

    def apsp(self) -> None:
        paths = self.floyd_warshall()
        for i, path in enumerate(paths):
            print(f"{i}: {path}")

    def dijkstra(self, start: int, end: int) -> List[int]:
        if not self.check_nodes_exist(start, end):
            return
        pq = PriorityQueue()

if __name__ == "__main__":
    network = Graph()
