import Network

def setup():
    network = Network.Network(6)
    edges1 = [
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
    ]
    edges2 = [
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
    for edge in edges1:
        network.add_edge(edge[0], edge[1], edge[2])
    network.print_nodes()
    # network.bfs(0,5)
    network.first_search(0,5,False)

if __name__ == "__main__":
    setup()
