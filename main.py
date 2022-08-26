import Graph


def setup():

    edge_list = [[
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
    solutions = {
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



    for i,edges in enumerate(edge_list):
        network = Graph.Graph(6)
        for edge in edges:
            network.add_edge(edge[0], edge[1], edge[2])
        # network.print_nodes()
        print()
        # for path_search in solutions:
        #     assert
        assert network.first_search(0, 5, True) == solutions['bfs'][i]
        print("=======")
        assert network.first_search(0, 5, False) == solutions['dfs'][i]
        print("=======")
        assert network.dijkstra(0,5) == solutions['dijkstra'][i]
        print("=======")
        assert network.mst(0) == solutions['mst'][i]
        print(solutions['mst'][i])
        print("=======")
        print("All-pairs shortest-paths:")
        network.apsp()
        print("---------------------")

if __name__ == "__main__":
    setup()
