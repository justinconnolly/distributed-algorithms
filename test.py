import unittest
import Graph

class GraphTest(unittest.TestCase):
    def setUp(self) -> None:
        self.edge_list = [
                [
                [0,1,1],
                [0,3,2],
                [1,2,2],
                [1,4,3],
                [1,3,3],
                [2,3,4],
                [2,4,1],
                [2,5,1],
                [3,4,5],
                [4,5,1]
            ],
            [
                [0,1,2],
                [0,3,1],
                [1,2,5],
                [1,4,3],
                [1,3,1],
                [2,3,1],
                [2,4,1],
                [2,5,5],
                [3,4,5],
                [4,5,1]
            ]
        ]

        self.start_end = [
            [0,5],
            [0,5]
        ]

        self.solutions = {
            'bfs': [
                [0, 1, 2, 5],
                [0, 1, 2, 5]
            ],
            'dfs': [
                [0, 3, 4, 5],
                [0, 3, 4, 5]
            ],
            'dijkstra': [
                [0, 1, 2, 5],
                [0, 3, 2, 4, 5]         
            ],
            'mst': [
                {1: 0, 3: 0, 2: 1, 4: 2, 5: 2},
                {1: 3, 3: 0, 2: 3, 4: 2, 5: 4}
            ]
        }
        self.graphs = []
        for i, edges in enumerate(self.edge_list):
            self.graphs.append(Graph.Graph(6))
            for edge in edges:
                self.graphs[-1].add_edge(edge[0], edge[1], edge[2])
   
    def test_paths(self):
        # for index, graph in enumerate(self.graphs):
        for i, v in enumerate(self.start_end):
            self.bfs_test(i,i)
            self.dfs_test(i,i)
            self.dijkstra_test(i)

    def bfs_test(self, graph, i):
        self.assertEqual(self.graphs[graph].first_search(self.start_end[i][0],self.start_end[i][1], True), self.solutions['bfs'][i])
        # self.assertEqual(self.graphs[i].first_search(5, 5, True), self.solutions['bfs'][i])

    def dfs_test(self, graph, i):
        self.assertEqual(self.graphs[graph].first_search(0, 5, False), self.solutions['dfs'][i])
    
    def dijkstra_test(self, i):
        self.assertEqual(self.graphs[i].dijkstra(0, 5), self.solutions['dijkstra'][i])

    def test_MST(self):
        for i, v in enumerate(self.edge_list):
            self.assertEqual(self.graphs[i].mst(0), self.solutions['mst'][i])

if __name__ == "__main__":
    unittest.main()