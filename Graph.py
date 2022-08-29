import math
from re import L
from typing import List, Callable
from PriorityQueue import PriorityQueue

class Digraph:
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

        def remove_edge(self, id):
            if id in self.neighbours:
                del self.neighbours[id]
                return True
            return False

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

        def __hash__(self):
            return hash(self.id)

        # def __eq__(self, other):
        #     return other.id == self.id
    
    def __init__(self, num_nodes: int = 1) -> None:
        self.nodes = {x: self.Node(x) for x in range(num_nodes)}
    
    def get_node(self, id: int) -> Node:
        if id >= len(self.nodes) or id < 0:
            return -1
        return self.nodes[id]

    def print_nodes(self) -> None:
        for node in self.nodes:
            node.print_neighbours()
    
    def add_node(self, val):
        self.nodes.append(self.Node(val))
        
    # this implies maybe I should have a set or dict id:index for O(1) rather than O(n)
    def contains(self, id: int) -> bool:
        if id in self.nodes:
            return True
        return False

    def add_node(self, id) -> bool:
        if id not in self.nodes:
            self.nodes[id] = self.Node(id)
            return True
        return False

    def remove_node(self, id) -> bool:
        if id not in self.nodes:
            return False
        del self.nodes[id]
        for node in self.nodes:
            if id in self.nodes[node].get_weighted_neighours():
                self.nodes[node].remove_edge(id)
        return True

    # def add_edge(self, node1, node2, weight):
    # def add_edge(self, new_edge: List[int]) -> None:
    def add_edge(self, node1: int, node2: int, weight: int):
        # node1, node2, weight = new_edge
        # self.get_node(node1).add_edge(self.get_node(node2), weight)
        # self.get_node(node2).add_edge(self.get_node(node1), weight)
        self.get_node(node1).add_edge(node2, weight)
        # self.get_node(node2).add_edge(node1, weight)
    
    # not strictly necessary because the edges are stored in dictionaries, but reasonable to have
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

    def check_nodes_exist(self, node1: int, node2: int) -> bool:
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
    def first_search(self, start: int, end: int, BFS: bool=False) -> List[int]:
        if not self.check_nodes_exist(start, end):
            return []
        if start == end:
            return [start]
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
                        return self.print_path(end, path)
                    seen.add(neighbour)
                    queue.append(neighbour)
        print("Unreachable.")
        return []

    def get_path_matrix(self) -> List[List[int]]:
        paths = [[math.inf for x in range(len(self.nodes))] for y in range(len(self.nodes))]
        for i,node in enumerate(self.nodes):
            paths[i][i] = 0
            for key in self.nodes[node].get_weighted_neighours():
                paths[i][key] = self.nodes[node].get_weight(key)
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
        return paths

    def dijkstra(self, start: int, end: int) -> List[int]:
        if not self.check_nodes_exist(start, end):
            return []
        print(f"Beginning Dijkstra's algorithm from {start} to {end}.")
        pq = PriorityQueue()
        dist = {start: 0}
        prev = {start: None}

        for node in self.nodes:
            if self.nodes[node].id != start:
                dist[self.nodes[node].id] = math.inf
                prev[self.nodes[node].id] = None
            pq.add(self.nodes[node].id, dist[self.nodes[node].id])

        while not pq.is_empty():
            curr = pq.get_min()
            neighbours = self.get_node(curr).get_weighted_neighours()
            for neighbour in neighbours:
                alt = dist[curr] + neighbours[neighbour]
                if alt < dist[neighbour] and dist[curr] is not math.inf and pq.contains(neighbour):
                    dist[neighbour] = alt
                    prev[neighbour] = curr
                    pq.decrease_key(neighbour, alt)
        return self.print_path(end, prev)



    def mst(self, start: int = 0):
        print(f"Beginning Prim's algorithm from {start}")
        curr = self.get_node(start)
        pq = PriorityQueue()
        seen = set([start])
        unseen = set([self.nodes[x].id for x in self.nodes])
        unseen.remove(start)
        edge_dict = {}
        for edge in curr.get_weighted_neighours():
            pq.add(edge, curr.get_weighted_neighours()[edge])
            edge_dict[edge] = start
        while not pq.is_empty():
            node = pq.get_min()
            seen.add(node)
            for neighbour in self.get_node(node).get_weighted_neighours():
                if neighbour not in seen:
                    if not pq.contains(neighbour):
                        pq.add(neighbour, self.get_node(node).get_weighted_neighours()[neighbour])
                        edge_dict[neighbour] = node
                    else:
                        if self.get_node(node).get_weighted_neighours()[neighbour] < pq.get_weight(neighbour):
                            pq.decrease_key(neighbour, self.get_node(node).get_weighted_neighours()[neighbour])
                            edge_dict[neighbour] = node
        return edge_dict


class Graph(Digraph):
    def __init__(self, num_nodes: int = 1) -> None:
        super().__init__(num_nodes)

    def add_edge(self, node1: int, node2: int, weight: int):
        self.get_node(node1).add_edge(node2, weight)
        self.get_node(node2).add_edge(node1, weight)

    def remove_node(self, id):
        if id not in self.nodes:
            return False
        for neighbour in self.get_node(id).get_weighted_neighours():
            self.nodes[neighbour].remove_edge(id)
        del self.nodes[id]
        return True


if __name__ == "__main__":
    network = Graph()
