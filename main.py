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
        [0,1,1],
        [0,3,2],
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
    bfs = [
        [0, 1, 2, 5],
        [0, 1, 2, 5]
    ]
    dfs = [
        [0, 3, 4, 5],
        [0, 3, 4, 5]
    ]
    # edges1 = [
    #     [0,1,1],
    #     [0,3,2],
    #     [1,2,2],
    #     [1,4,3],
    #     [1,3,3],
    #     [2,3,4],
    #     [2,4,1],
    #     [2,5,1],
    #     [3,4,5],
    #     [4,5,1]
    # ]
    # edges2 = [
    #     [0,1,1],
    #     [0,3,2],
    #     [1,2,5],
    #     [1,4,3],
    #     [1,3,1],
    #     [2,3,1],
    #     [2,4,1],
    #     [2,5,5],
    #     [3,4,5],
    #     [4,5,1]
    # ]
    for i,edges in enumerate(edge_list):
        network = Graph.Graph(6)
        for edge in edges:
            network.add_edge(edge)
        network.print_nodes()
        assert network.first_search(0, 5, True) == bfs[i]
        assert network.first_search(0, 5, False) == dfs[i]
    # network.get_all_pairs_paths()
        network.apsp()

if __name__ == "__main__":
    setup()
