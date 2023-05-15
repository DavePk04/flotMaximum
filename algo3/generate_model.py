import sys

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


def remove_loops(graph):
    n = len(graph)
    for i in range(n):
        if graph[i][i] > 0:
            graph[i][i] = 0
    return graph



# call the parse_input_file function and the ford_fulkerson function to find the maximum flow
n, s, t, graph = parse_input_file(filename)


# function to solve the maximum flow problem using glpk solve
# this program is wrote in model-n-p.lp file
# objective function: maximize the flow from the source to the sink (it's the sum of the outgoing edges from the source)
# constraints: for each node i except the source and the sink, , sum of incoming edges - sum of outgoing edges = 0
#              for the source node, sum of outgoing edges >= 0
#              for the sink node, sum of incoming edges <= 0
# Bounds: for each edge (i, j), the flow on the edge >= 0 and <= capacity of the edge
def write_model(n, s, t, graph):
    with open("model-n-p.lp", 'w') as f:
        f.write("Maximize\n")
        f.write(" obj: ")
        outgoing_edges = [j for j in range(n) if graph[s][j] > 0]
        for j in outgoing_edges:
            f.write(" + x{}_{}".format(s, j))
        f.write("\n\n")

        f.write("Subject To\n")
        for i in range(n):
            if i != s and i != t:
                f.write(" c{}: ".format(i))
                incoming_edges = [j for j in range(n) if graph[j][i] > 0]
                outgoing_edges = [j for j in range(n) if graph[i][j] > 0]
                for j in incoming_edges:
                    f.write(" + x{}_{}".format(j, i))
                for j in outgoing_edges:
                    f.write(" - x{}_{}".format(i, j))
                f.write(" = 0\n")

        f.write(" c{}: ".format(s))
        for j in outgoing_edges:
            f.write(" + x{}_{}".format(s, j))
        f.write(" = 0\n")

        f.write(" c{}: ".format(t))
        incoming_edges = [j for j in range(n) if graph[j][t] > 0]
        for j in incoming_edges:
            f.write(" + x{}_{}".format(j, t))
        f.write(" = 0\n\n")

        f.write("Bounds\n")
        for i in range(n):
            for j in range(n):
                if graph[i][j] > 0:
                    f.write(" 0 <= x{}_{} <= {}\n".format(i, j, graph[i][j]))

        f.write("\n\n")

        f.write("Binary\n")
        for i in range(n):
            for j in range(n):
                if graph[i][j] > 0:
                    f.write(" x{}_{}\n".format(i, j))

        f.write("End\n")


# remove loops from the graph
graph = remove_loops(graph)
# call the write_model function
write_model(n, s, t, graph)


