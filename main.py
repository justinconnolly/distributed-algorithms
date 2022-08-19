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
            [0, 1, 4, 5]          
        ]
    }

    bfs = [
        [0, 1, 2, 5],
        [0, 1, 2, 5]
    ]
    dfs = [
        [0, 3, 4, 5],
        [0, 3, 4, 5]
    ]
    dijkstra = [
        [0, 1, 2, 5],
        [0, 1, 4, 5]
    ]


    for i,edges in enumerate(edge_list):
        network = Graph.Graph(6)
        for edge in edges:
            network.add_edge(edge[0], edge[1], edge[2])
        # network.print_nodes()
        print()
        # for path_search in solutions:
        #     assert
        assert network.first_search(0, 5, True) == solutions['bfs'][i]
        assert network.first_search(0, 5, False) == solutions['dfs'][i]
        assert network.dijkstra(0,5) == solutions['dijkstra'][i]
        network.apsp()
        print("---------------------")

if __name__ == "__main__":
    setup()
