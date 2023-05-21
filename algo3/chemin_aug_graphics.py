import matplotlib.pyplot as plt

def read_data_from_file(file_path):
    data = {}
    with open(file_path, 'r') as file:
        lines = file.readlines()

    instance = None
    elapsed_time = None
    instance_type = None
    size = None

    for line in lines:
        line = line.strip()
        if line.startswith("Instance:"):
            instance = line.split(":")[1].strip()
            instance_type = int(instance.split("-")[-1].split(".")[1])
            size = int(instance.split("-")[-2])
        elif line.startswith("Elapsed Time:"):
            elapsed_time = float(line.split(":")[1].strip().split()[0])

        if instance is not None:
            data[instance] = {"size": size, "type": instance_type, "time": elapsed_time}

    return data

def build_graph(data, instance_type):
    sizes = []
    times = []

    for key, value in data.items():
        if value['type'] == instance_type:
            sizes.append(value['size'])
            times.append(value['time'])

    sizes, times = zip(*sorted(zip(sizes, times)))  # Tri des listes sizes et times en fonction de sizes
    print(f"Sizes: {sizes}\nTimes: {times}\n")
    plt.plot(times, sizes, marker='o')
    plt.ylabel("Taille des instances de type {}".format(instance_type))
    plt.xlabel('Temps de résolution (en secondes)')
    plt.title('glpk: taille des instances = f(temps de résolution)')
    plt.show()

file_path = input("Enter the file path: ")
data = read_data_from_file(file_path)

build_graph(data, 1)
build_graph(data, 2)
build_graph(data, 3)
