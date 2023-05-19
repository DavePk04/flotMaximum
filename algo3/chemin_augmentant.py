import argparse
import math
from collections import deque, defaultdict
import time


class FordFulkerson:
    """
    Implementation of the Ford-Fulkerson algorithm to compute the maximum flow in a network.
    """

    def __init__(self, filename):
        self._filename = filename
        self._graph = []
        self._n = 0
        self._s = 0
        self._t = 0
        self._max_flow = 0
        self._parse_input_file()
        self._remove_loops()
        self._remove_incoming_arcs_to_s()
        self._remove_outgoing_arcs_from_t()
        self._compute_max_flow()
        self._calculate_max_flow_st_cut()

    def _parse_input_file(self):
        """
        Parse the input file and store the graph data in the class attributes.
        """
        with open(self._filename, 'r') as f:
            self._n = int(f.readline().split()[1])
            self._s = int(f.readline().split()[1])
            self._t = int(f.readline().split()[1])
            num_arcs = int(f.readline().split()[1])
            self._graph = [[0] * self._n for _ in range(self._n)]
            for _ in range(num_arcs):
                u, v, capacity = map(int, f.readline().split())
                self._graph[u][v] = capacity

    def _bfs(self, parent):
        """
        Breadth-first search to find an augmenting path from source to sink.
        """
        queue = deque([self._s])
        visited = set(queue)
        while queue:
            u = queue.popleft()
            for v, capacity in enumerate(self._graph[u]):
                if capacity > 0 and v not in visited:
                    queue.append(v)
                    visited.add(v)
                    parent[v] = u
                    if v == self._t:
                        return True
        return False

    def _compute_max_flow(self, time_limit=300):
        """
        Compute the maximum flow using the Ford-Fulkerson algorithm.
        """
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

    def _remove_loops(self):
        """
        Remove self-loops in the graph by setting the corresponding capacities to 0.
        """
        for i in range(self._n):
            self._graph[i][i] = 0

    def _remove_incoming_arcs_to_s(self):
        """
        Remove incoming arcs to the source node by setting their capacities to 0.
        """
        for i in range(self._n):
            self._graph[i][self._s] = 0

    def _remove_outgoing_arcs_from_t(self):
        """
        Remove outgoing arcs from the sink node by setting their capacities to 0.
        """
        for i in range(self._n):
            self._graph[self._t][i] = 0

    def _calculate_max_flow_st_cut(self):
        """
        Calculate the flow across the minimum cut between the source and sink nodes.
        """
        visited = set()
        queue = deque([self._s])
        visited.add(self._s)

        while queue:
            u = queue.popleft()
            for v, capacity in enumerate(self._graph[u]):
                if capacity > 0 and v not in visited:
                    queue.append(v)
                    visited.add(v)

        st_cut_flow = sum(
            self._graph[v][u]
            for u in visited
            for v, capacity in enumerate(self._graph[u])
            if v not in visited and capacity == 0
        )

        if st_cut_flow == self._max_flow:
            print("Le flot maximal est optimal")
        else:
            print("Le flot maximal n'est pas optimal")

    def get_max_flow(self):
        """
        Get the maximum flow value.
        """
        return self._max_flow

    def save_result(self, filename=None):
        if filename is None:
            filename = f"model-{self._filename.replace('Instances/inst-', '').replace('.txt', '')}.path"
        with open(filename, 'w') as f:
            f.write(f"Le flot maximal est : {self._max_flow}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Ford-Fulkerson algorithm')
    parser.add_argument('filename', type=str, help='input file')
    args = parser.parse_args()

    ford_fulkerson = FordFulkerson(args.filename)
    maxflow = ford_fulkerson.get_max_flow()
    ford_fulkerson.save_result()
    print(f"Le flot maximal est : {maxflow}")
