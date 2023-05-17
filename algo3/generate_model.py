import sys
import os

class MaxFlowSolver:
    def __init__(self, filename):
        self.filename = filename
        self.n = 0
        self.s = 0
        self.t = 0
        self.graph = []

    def solve(self):
        self.parse_input_file()
        self.remove_cycles()
        self.write_model()

    def parse_input_file(self):
        with open(self.filename, 'r') as f:
            lines = f.readlines()
            self.n = int(lines[0].split()[1]) # number of nodes
            self.s = int(lines[1].split()[1]) # source node
            self.t = int(lines[2].split()[1]) # sink node
            num_arcs = int(lines[3].split()[1]) # number of edges
            self.graph = [[0] * self.n for _ in range(self.n)] # initialize the adjacency matrix with zeros
            for line in lines[4:4 + num_arcs]:
                u, v, capacity = map(int, line.split())
                self.graph[u][v] = capacity  # set edge capacity

    def remove_cycles(self):
        for i in range(self.n):
            self.graph[i][i] = 0 # remove self-loops
            for j in range(i + 1, self.n):
                if self.graph[i][j] > 0 and self.graph[j][i] > 0:
                    # If there is an edge from i to j and an edge from j to i, remove the edge from j to i
                    self.graph[j][i] = 0

    def get_model_filename(self):
        file_name_without_ext = os.path.splitext(self.filename)[0]
        file_parts = file_name_without_ext.split("-")
        n = file_parts[1]
        p = file_parts[2]
        model_filename = "model-{}.lp".format("-".join([n, p]))
        return model_filename

    def write_model(self):
        model_filename = self.get_model_filename()
        with open(model_filename, 'w') as f:
            f.write("Maximize\n")
            f.write(" obj: ")
            outgoing_edges = [j for j in range(self.n) if self.graph[self.s][j] > 0]
            for j in outgoing_edges:
                f.write(" + x{}_{}".format(self.s, j))
            f.write("\n\n")

            f.write("Subject To\n")
            for i in range(self.n):
                if i != self.s and i != self.t:
                    f.write(" c{}: ".format(i))
                    incoming_edges = [j for j in range(self.n) if self.graph[j][i] > 0]
                    outgoing_edges = [j for j in range(self.n) if self.graph[i][j] > 0]
                    for j in incoming_edges:
                        f.write(" - x{}_{}".format(j, i))
                    for j in outgoing_edges:
                        f.write(" + x{}_{}".format(i, j))
                    f.write(" = 0\n")
            # constraint for the source node
            f.write(" c{}: ".format(self.s))
            outgoing_edges = [j for j in range(self.n) if self.graph[self.s][j] > 0]
            for j in outgoing_edges:
                f.write(" + x{}_{}".format(self.s, j))
            f.write(" >= 0\n")

            # constraint for the sink node
            f.write(" c{}: ".format(self.t))
            incoming_edges = [j for j in range(self.n) if self.graph[j][self.t] > 0]
            for j in incoming_edges:
                f.write(" - x{}_{}".format(j, self.t))
            f.write(" <= 0\n\n")

            f.write("Bounds\n")
            for i in range(self.n):
                for j in range(self.n):
                    if self.graph[i][j] > 0:
                        f.write(" 0 <= x{}_{} <= {}\n".format(i, j, self.graph[i][j]))

            f.write("\n\n")

            f.write("Binary\n")
            for i in range(self.n):
                for j in range(self.n):
                    if self.graph[i][j] > 0:
                        f.write(" x{}_{}\n".format(i, j))

            f.write("\n\nEnd\n")


if __name__ == "__main__":
    try:
        filename = sys.argv[1]
        solver = MaxFlowSolver(filename)
        solver.solve()
    except IndexError:
        print("Usage: python3 generate_model.py <filename>")
        sys.exit(1)
