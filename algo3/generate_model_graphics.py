import matplotlib.pyplot as plt
import numpy as np

data = {
    "inst-100-0.1.txt": {"size": 100, "type": 1, "time": 0.023894071578979492},
    "inst-100-0.2.txt": {"size": 100, "type": 2, "time": 0.022114038467407227},
    "inst-100-0.3.txt": {"size": 100, "type": 3, "time": 0.03557300567626953},
    "inst-200-0.1.txt": {"size": 200, "type": 1, "time": 0.02935194969177246},
    "inst-200-0.2.txt": {"size": 200, "type": 2, "time": 0.050570011138916016},
    "inst-300-0.1.txt": {"size": 300, "type": 1, "time": 0.06082606315612793},
    "inst-200-0.3.txt": {"size": 200, "type": 3, "time": 0.07380890846252441},
    "inst-400-0.1.txt": {"size": 400, "type": 1, "time": 0.09353280067443848},
    "inst-300-0.2.txt": {"size": 300, "type": 2, "time": 0.11107993125915527},
    "inst-500-0.1.txt": {"size": 500, "type": 1, "time": 0.15097498893737793},
    "inst-300-0.3.txt": {"size": 300, "type": 3, "time": 0.18001890182495117},
    "inst-400-0.2.txt": {"size": 400, "type": 2, "time": 0.2138988971710205},
    "inst-600-0.1.txt": {"size": 600, "type": 1, "time": 0.2617990970611572},
    "inst-400-0.3.txt": {"size": 400, "type": 3, "time": 0.3765718936920166},
    "inst-700-0.1.txt": {"size": 700, "type": 1, "time": 0.39200401306152344},
    "inst-500-0.2.txt": {"size": 500, "type": 2, "time": 0.40821194648742676},
    "inst-800-0.1.txt": {"size": 800, "type": 1, "time": 0.5717158317565918},
    "inst-600-0.2.txt": {"size": 600, "type": 2, "time": 0.6044728755950928},
    "inst-500-0.3.txt": {"size": 500, "type": 3, "time": 0.5462188720703125},
    "inst-900-0.1.txt": {"size": 900, "type": 1, "time": 0.7499089241027832},
    "inst-700-0.2.txt": {"size": 700, "type": 2, "time": 0.8977971076965332},
    "inst-1000-0.1.txt": {"size": 1000, "type": 1, "time": 0.8358819484710693},
    "inst-600-0.3.txt": {"size": 600, "type": 3, "time": 1.0554187297821045},
    "inst-1100-0.1.txt": {"size": 1100, "type": 1, "time": 1.0524718761444092},
    "inst-800-0.2.txt": {"size": 800, "type": 2, "time": 1.175367832183838},
    "inst-700-0.3.txt": {"size": 700, "type": 3, "time": 1.650974988937378},
    "inst-1200-0.1.txt": {"size": 1200, "type": 1, "time": 1.5403189659118652},
    "inst-900-0.2.txt": {"size": 900, "type": 2, "time": 1.58394193649292},
    "inst-1300-0.1.txt": {"size": 1300, "type": 1, "time": 1.9953579902648926},
    "inst-800-0.3.txt": {"size": 800, "type": 3, "time": 2.254836082458496},
    "inst-1000-0.2.txt": {"size": 1000, "type": 2, "time": 2.08565616607666},
    "inst-1400-0.1.txt": {"size": 1400, "type": 1, "time": 1.992337942123413},
    "inst-900-0.3.txt": {"size": 900, "type": 3, "time": 3.0949440002441406},
    "inst-1500-0.1.txt": {"size": 1500, "type": 1, "time": 2.488821029663086},
    "inst-1100-0.2.txt": {"size": 1100, "type": 2, "time": 3.4005520343780518},
    "inst-1000-0.3.txt": {"size": 1000, "type": 3, "time": 4.299808979034424},
    "inst-1200-0.2.txt": {"size": 1200, "type": 2, "time": 4.001800060272217},
    "inst-1300-0.2.txt": {"size": 1300, "type": 2, "time": 4.899011850357056},
    "inst-1100-0.3.txt": {"size": 1100, "type": 3, "time": 5.679090976715088},
    "inst-1400-0.2.txt": {"size": 1400, "type": 2, "time": 5.901246070861816},
    "inst-1200-0.3.txt": {"size": 1200, "type": 3, "time": 6.681480884552002},
    "inst-1500-0.2.txt": {"size": 1500, "type": 2, "time": 7.977987051010132},
    "inst-1300-0.3.txt": {"size": 1300, "type": 3, "time": 9.004582166671753},
    "inst-1400-0.3.txt": {"size": 1400, "type": 3, "time": 10.235420942306519},
    "inst-1500-0.3.txt": {"size": 1500, "type": 3, "time": 12.030403137207031}
}


def build_graph(data, type):
    sizes = []
    times = []

    for key, value in data.items():
        if value['type'] == type:
            sizes.append(value['size'])
            times.append(value['time'])

    plt.plot(times, sizes, marker='o')
    plt.ylabel("Taille des instances de type {}".format(type))
    plt.xlabel('Temps de résolution (en secondes)')
    plt.title('glpk: taille des instances = f(temps de résolution)')
    plt.show()

# FIXME: ecart type
def ecart_type(data, type):
    times = []

    for key, value in data.items():
        if value['type'] == type:
            times.append(value['time'])

    return np.std(times)


build_graph(data, 1)
build_graph(data, 2)
build_graph(data, 3)