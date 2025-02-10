# Adjacency matrix for an unweighted, undirected graph
graph = [
    [0, 1, 1, 0],  # Vertex 0 is connected to vertices 1 and 2
    [1, 0, 1, 1],  # Vertex 1 is connected to vertices 0, 2, and 3
    [1, 1, 0, 1],  # Vertex 2 is connected to vertices 0, 1, and 3
    [0, 1, 1, 0],  # Vertex 3 is connected to vertices 1 and 2
]

# Check if there's an edge between vertex 0 and vertex 2:
if graph[0][2] == 1:
    print("There is an edge between vertex 0 and vertex 2")