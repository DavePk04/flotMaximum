import argparse
import os


class GenerateModel:
    def __init__(self):
        self._n = 0  # number of nodes
        self._s = 0  # source
        self._t = 0  # sink
        self._arcs = []  # list of arcs (i, j, capacity)
        self._output_file = ""

    def _parse_instance_file(self, instance_file):
        with open(instance_file, 'r') as f:
            self._n = int(f.readline().split()[1])
            self._s = int(f.readline().split()[1])
            self._t = int(f.readline().split()[1])
            num_arcs = int(f.readline().split()[1])
            for _ in range(num_arcs):
                i, j, capacity = map(int, f.readline().split())
                self._arcs.append((i, j, capacity))

    def _generate_model(self):
        model = "Maximize\n obj: " + f"Flot_{self._s}_{self._t}\n\nSubject To\n"

        # contrainte de capacité pour chaque arc
        for i, j, capacity in self._arcs:
            model += f" c{i}_{j}: Flot_{i}_{j} <= {capacity}\n"

        # Contraintes de conservation du flot pour chaque nœud intermédiaire
        for node in range(1, self._n + 1):
            if node != self._s and node != self._t:
                in_flow = [f"Flot_{i}_{node}" for i, j, c in self._arcs if j == node]
                out_flow = [f"Flot_{node}_{j}" for i, j, c in self._arcs if i == node]

                model += f" c{node}: {' + '.join(in_flow)} - {' + '.join(out_flow)} = 0\n"

        # Contrainte de flot sortant de la source
        out_flow = [f"Flot_{self._s}_{j}" for i, j, c in self._arcs if i == self._s]
        model += f" c{self._s}: {' + '.join(out_flow)} = 1\n"

        # Contrainte de flot entrant dans le puits
        in_flow = [f"Flot_{i}_{self._t}" for i, j, c in self._arcs if j == self._t]
        model += f" c{self._t}: {' + '.join(in_flow)} = 1\n"

        # Variables de flot
        model += "\nBinary\n"
        for i, j, c in self._arcs:
            model += f" Flot_{i}_{j}\n"

        model += "\nEnd"

        return model

    def _save_model(self, model):
        models_dir = "models"
        os.makedirs(models_dir, exist_ok=True)

        model_path = os.path.join(models_dir, self._output_file)
        with open(model_path, 'w') as f:
            f.write(model)

        print(f"Le modèle a été généré avec succès dans le fichier {model_path}\n\n")

    def generate(self, instance_file):
        self._parse_instance_file(instance_file)
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

    # Appel à glpsol pour résoudre le modèle
    ouptut_file = generator.get_output_file()
    os.system(f"glpsol --tmlim 300 --lp models/{ouptut_file} -o solutions/{ouptut_file.replace('lp', 'sol')}")
