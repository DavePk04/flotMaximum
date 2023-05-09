import sys

# BFS algorithm to find a path from source to sink
def bfs(graph, s, t, parent):
    visited = [False] * len(graph) # mark all nodes as unvisited
    queue = [s] # start from the source node
    visited[s] = True # mark the source node as visited
    while queue:
        u = queue.pop(0) # dequeue a node
        for ind, val in enumerate(graph[u]):
            # if a node is not visited and there is a positive capacity edge
            if not visited[ind] and val > 0:
                queue.append(ind) # enqueue the node
                visited[ind] = True # mark the node as visited
                parent[ind] = u # update the parent of the node
    return visited[t] # return True if there is a path from source to sink

# Ford-Fulkerson algorithm to find the maximum flow
def ford_fulkerson(graph, source, sink):
    parent = [-1] * len(graph) # initialize the parent list with -1
    max_flow = 0 # initialize the maximum flow as 0
    while bfs(graph, source, sink, parent):
        path_flow = float("Inf") # initialize the path flow as infinity
        s = sink
        # find the minimum residual capacity along the path from sink to source
        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]
        max_flow += path_flow # add the path flow to the maximum flow
        v = sink
        # update the residual capacities of the edges and their reverse edges along the path
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]
    return max_flow # return the maximum flow

filename = ""
if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    print("Argument manquant")

# parse the input file
def parse_input_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        n = int(lines[0].split()[1]) # number of nodes
        s = int(lines[1].split()[1]) # source node
        t = int(lines[2].split()[1]) # sink node
        num_arcs = int(lines[3].split()[1]) # number of edges
        graph = [[0] * n for i in range(n)] # initialize the adjacency matrix with zeros
        for i in range(4, 4 + num_arcs):
            u, v, capacity = map(int, lines[i].split())
            graph[u][v] = capacity # set the capacity of the edge
        return n, s, t, graph

# call the parse_input_file function and the ford_fulkerson function to find the maximum flow
n, s, t, graph = parse_input_file(filename)
max_flow = ford_fulkerson(graph, s, t)

# print the maximum flow
print("Le flot maximal est : ", max_flow)
