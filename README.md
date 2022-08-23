# Distributed and Graph Algorithms

Practice for some distributed and graph algorithms. The idea is the emulate a distributed network as reasonably as possible in order to properly implement things like leader election without cheating (ie letting the nodes decide rather than just iterating over the graph). Implementing something like Diffie-Hellman key exchange between nodes might be a thing to dip my toes into cryptography.

Ideally this turns into a reasonable testing platform for COMP4001 - Distributed Computing and COMP5900 - Multiagent Systems, and is useable for COMP2804 - Discrete Structures II and COMP3804 - Design and Analysis of Algorithms I



## TODO
Cycle detection, A*, Bellman-Ford, leader election, maybe network flow and Diffie-Hellman, updated methods to allow for digraphs (everything is essentially an undirected graph because add_edge adds the edge to both nodes).

## DONE
Adding weighted edges, BFS, DFS, Floyd-Warshall APSP, Dijkstra, priority queue (to be used), Prim's algorithm for MST