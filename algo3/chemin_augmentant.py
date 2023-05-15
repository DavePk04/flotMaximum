import sys

class MaxFlowSolver:
    def __init__(self, filename):
        self.filename = filename
        self.graph = []
        self.n = 0
        self.s = 0
        self.t = 0

    def solve(self):
        self.parse_input_file()
        max_flow = self.ford_fulkerson()
        print("maximal flow: {}".format(max_flow))

    def parse_input_file(self):
        with open(self.filename, 'r') as f:
            lines = f.readlines()
            self.n = int(lines[0].split()[1])  # number of nodes
            self.s = int(lines[1].split()[1])  # source node
            self.t = int(lines[2].split()[1])  # sink node
            num_arcs = int(lines[3].split()[1])  # number of edges
            self.graph = [[0] * self.n for _ in range(self.n)]  # initialize the adjacency matrix with zeros
            for i in range(4, 4 + num_arcs):
                u, v, capacity = map(int, lines[i].split())
                self.graph[u][v] = capacity  # set the capacity of the edge

    def bfs(self, parent):
        visited = [False] * len(self.graph)  # mark all nodes as unvisited
        queue = [self.s]  # start from the source node
        visited[self.s] = True  # mark the source node as visited
        while queue:
            u = queue.pop(0)  # dequeue a node
            for ind, val in enumerate(self.graph[u]):
                # if a node is not visited and there is a positive capacity edge
                if not visited[ind] and val > 0:
                    queue.append(ind)  # enqueue the node
                    visited[ind] = True  # mark the node as visited
                    parent[ind] = u  # update the parent of the node
        return visited[self.t]  # return True if there is a path from source to sink

    def ford_fulkerson(self):
        parent = [-1] * len(self.graph)  # initialize the parent list with -1
        max_flow = 0  # initialize the maximum flow as 0
        while self.bfs(parent):
            path_flow = float("Inf")  # initialize the path flow as infinity
            s = self.t
            # find the minimum residual capacity along the path from sink to source
            while s != self.s:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]
            max_flow += path_flow  # add the path flow to the maximum flow
            v = self.t
            # update the residual capacities of the edges and their reverse edges along the path
            while v != self.s:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
        return max_flow  # return the maximum flow


if __name__ == '__main__':
    try:
        solver = MaxFlowSolver(sys.argv[1])
        solver.solve()
    except IndexError:
        print("Usage: python chemin_augmentant.py <filename>")
        sys.exit(1)