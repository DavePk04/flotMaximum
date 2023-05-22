import argparse
import os
import time


class GenerateModel:
    """
    Generate a model for the maximum flow problem in the format of CPLEX LP files.
    """
    def __init__(self):
        self._n = 0  # number of nodes
        self._s = 0  # source
        self._t = 0  # sink
        self._graph = []  # list of arcs (i, j, capacity)
        self._output_file = ""

    def _parse_instance_file(self, instance_file):
        with open(instance_file, 'r') as f:
            self._n = int(f.readline().split()[1])
            self._s = int(f.readline().split()[1])
            self._t = int(f.readline().split()[1])
            num_arcs = int(f.readline().split()[1])
            self._graph = [[0] * self._n for _ in range(self._n)]
            for i in range(4, num_arcs + 4):
                u, v, capacity = map(int, f.readline().split())
                self._graph[u][v] = capacity

    def _remove_loops(self):
        for i in range(self._n):
            self._graph[i][i] = 0

    def _remove_incoming_arcs_to_s(self):
        for i in range(self._n):
            self._graph[i][self._s] = 0

    def _remove_outgoing_arcs_from_t(self):
        for i in range(self._n):
            self._graph[self._t][i] = 0

    def _generate_model(self):
        lines = ["Maximize"]
        lines.append(" obj: " + " + ".join([f"f{self._s}_{j}" for j in range(self._n) if self._graph[self._s][j] > 0]))

        lines.append("\nSubject To")
        for i in range(self._n):
            if i != self._s and i != self._t:
                incoming_edges = [j for j in range(self._n) if self._graph[j][i] > 0]
                outgoing_edges = [j for j in range(self._n) if self._graph[i][j] > 0]
                lines.append(f" c{i}: " + " + ".join([f"f{j}_{i}" for j in incoming_edges]) + " - " + " - ".join(
                    [f"f{i}_{j}" for j in outgoing_edges]) + " = 0")

        outgoing_edges = [j for j in range(self._n) if self._graph[self._s][j] > 0]
        lines.append(f" c{self._s}: " + " + ".join([f"f{self._s}_{j}" for j in outgoing_edges]) + " >= 0")

        incoming_edges = [j for j in range(self._n) if self._graph[j][self._t] > 0]
        lines.append(f" c{self._t}: " + " + ".join([f"f{j}_{self._t}" for j in incoming_edges]) + " >= 0")

        lines.append("\nBounds")
        for i in range(self._n):
            for j in range(self._n):
                if self._graph[i][j] > 0:
                    lines.append(f" 0 <= f{i}_{j} <= {self._graph[i][j]}")

        lines.append("\nEnd")

        return "\n".join(lines)

    def _save_model(self, model):
        with open(self._output_file, 'w') as f:
            f.write(model)
        print(f"The model has been successfully generated in the file {self._output_file}\n\n")

    def generate(self, instance_file):
        self._parse_instance_file(instance_file)
        self._remove_loops()
        self._remove_incoming_arcs_to_s()
        self._remove_outgoing_arcs_from_t()
        model = self._generate_model()
        self._output_file = f"model-{instance_file.replace('Instances/inst-', '').replace('.txt', '')}.lp"
        self._save_model(model)

    def get_output_file(self):
        return self._output_file


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate model from instance file')
    parser.add_argument('instance_file', type=str, help='instance file')
    args = parser.parse_args()

    generator = GenerateModel()
    generator.generate(args.instance_file)

    output_file = generator.get_output_file()
    solution_file = output_file.replace(".lp", ".sol")

    start_time = time.time()
    os.system(f"glpsol --tmlim 300 --lp {output_file} -o {solution_file}")
    end_time = time.time()
    print(f"Time: {end_time - start_time} seconds")
    print(f"Solution has been generated successfully in the file {solution_file}\n")
