import argparse
import math
from collections import deque, defaultdict
import time


class FordFulkerson:
    def __init__(self, filename):
        self._filename = filename
        self._graph = None
        self._n = 0
        self._s = 0
        self._t = 0
        self._max_flow = 0
        self._parse_input_file()
        self._compute_max_flow()

    def _parse_input_file(self):
        with open(self._filename, 'r') as f:
            self._n = int(f.readline().split()[1])
            self._s = int(f.readline().split()[1])
            self._t = int(f.readline().split()[1])
            num_arcs = int(f.readline().split()[1])
            self._graph = defaultdict(dict)
            for _ in range(num_arcs):
                u, v, capacity = map(int, f.readline().split())
                self._graph.setdefault(u, {})[v] = capacity
                self._graph.setdefault(v, {})[u] = 0

    def _bfs(self, parent):
        queue = deque([self._s])
        visited = set(queue)
        while queue:
            u = queue.popleft()
            for v, capacity in self._graph[u].items():
                if capacity > 0 and v not in visited:
                    queue.append(v)
                    visited.add(v)
                    parent[v] = u
                    if v == self._t:
                        return True
        return False

    def _compute_max_flow(self, time_limit=300):
        parent = [-1] * self._n
        self._max_flow = 0
        start_time = time.time()
        while self._bfs(parent):
            path_flow = math.inf
            v, u = self._t, parent[self._t]
            while v != self._s:
                path_flow = min(path_flow, self._graph[u][v])
                v, u = u, parent[u]
            self._max_flow += path_flow
            v, u = self._t, parent[self._t]
            while v != self._s:
                self._graph[u][v] -= path_flow
                self._graph[v][u] += path_flow
                v, u = u, parent[u]

            elapsed_time = time.time() - start_time
            if elapsed_time > time_limit:
                break

    def get_max_flow(self):
        return self._max_flow

    def save_result(self, filename=None):
        if filename is None:
            filename = f"model-{self._filename.replace('Instances/inst-', '').replace('.txt', '')}.path"
        with open(filename, 'w') as f:
            f.write(f"Le flot maximal est : {self._max_flow}")

    def get_graph(self):
        return self._graph


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Ford-Fulkerson algorithm')
    parser.add_argument('filename', type=str, help='input file')
    args = parser.parse_args()

    ford_fulkerson = FordFulkerson(args.filename)
    maxflow = ford_fulkerson.get_max_flow()
    ford_fulkerson.save_result()
    print(f"Le flot maximal est : {maxflow}")