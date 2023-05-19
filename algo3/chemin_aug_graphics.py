import matplotlib.pyplot as plt

data = {
    "Instances/inst-100-0.1.txt": {"size": 100, "type": 1, "time": 0.010528802871704102},
    "Instances/inst-100-0.2.txt": {"size": 100, "type": 2, "time": 0.014394044876098633},
    "Instances/inst-100-0.3.txt": {"size": 100, "type": 3, "time": 0.0207369327545166},
    "Instances/inst-200-0.1.txt": {"size": 200, "type": 1, "time": 0.05821800231933594},
    "Instances/inst-200-0.2.txt": {"size": 200, "type": 2, "time": 0.11075687408447266},
    "Instances/inst-300-0.1.txt": {"size": 300, "type": 1, "time": 0.20030713081359863},
    "Instances/inst-200-0.3.txt": {"size": 200, "type": 3, "time": 0.15941715240478516},
    "Instances/inst-400-0.1.txt": {"size": 400, "type": 1, "time": 0.442018985748291},
    "Instances/inst-300-0.2.txt": {"size": 300, "type": 2, "time": 0.3750479221343994},
    "Instances/inst-500-0.1.txt": {"size": 500, "type": 1, "time": 0.6899187564849854},
    "Instances/inst-300-0.3.txt": {"size": 300, "type": 3, "time": 0.5195541381835938},
    "Instances/inst-400-0.2.txt": {"size": 400, "type": 2, "time": 0.8772919178009033},
    "Instances/inst-600-0.1.txt": {"size": 600, "type": 1, "time": 1.8656020164489746},
    "Instances/inst-400-0.3.txt": {"size": 400, "type": 3, "time": 1.390197992324829},
    "Instances/inst-700-0.1.txt": {"size": 700, "type": 1, "time": 2.482717990875244},
    "Instances/inst-500-0.2.txt": {"size": 500, "type": 2, "time": 1.9663147926330566},
    "Instances/inst-800-0.1.txt": {"size": 800, "type": 1, "time": 4.0495030879974365},
    "Instances/inst-600-0.2.txt": {"size": 600, "type": 2, "time": 3.1199889183044434},
    "Instances/inst-500-0.3.txt": {"size": 500, "type": 3, "time": 2.5469870567321777},
    "Instances/inst-900-0.1.txt": {"size": 900, "type": 1, "time": 5.417770147323608},
    "Instances/inst-700-0.2.txt": {"size": 700, "type": 2, "time": 5.649713754653931},
    "Instances/inst-1000-0.1.txt": {"size": 1000, "type": 1, "time": 7.807745933532715},
    "Instances/inst-600-0.3.txt": {"size": 600, "type": 3, "time": 4.484086036682129},
    "Instances/inst-1100-0.1.txt": {"size": 1100, "type": 1, "time": 11.2503342628479},
    "Instances/inst-800-0.2.txt": {"size": 800, "type": 2, "time": 7.064451217651367},
    "Instances/inst-700-0.3.txt": {"size": 700, "type": 3, "time": 7.9892919063568115},
    "Instances/inst-1200-0.1.txt": {"size": 1200, "type": 1, "time": 14.665380954742432},
    "Instances/inst-900-0.2.txt": {"size": 900, "type": 2, "time": 11.831470012664795},
    "Instances/inst-1300-0.1.txt": {"size": 1300, "type": 1, "time": 17.04933786392212},
    "Instances/inst-800-0.3.txt": {"size": 800, "type": 3, "time": 12.424888849258423},
    "Instances/inst-1000-0.2.txt": {"size": 1000, "type": 2, "time": 14.598401069641113},
    "Instances/inst-1400-0.1.txt": {"size": 1400, "type": 1, "time": 21.500918865203857},
    "Instances/inst-900-0.3.txt": {"size": 900, "type": 3, "time": 17.378129243850708},
    "Instances/inst-1500-0.1.txt": {"size": 1500, "type": 1, "time": 26.776742935180664},
    "Instances/inst-1100-0.2.txt": {"size": 1100, "type": 2, "time": 22.024914979934692},
    "Instances/inst-1000-0.3.txt": {"size": 1000, "type": 3, "time": 24.088107109069824},
    "Instances/inst-1200-0.2.txt": {"size": 1200, "type": 2, "time": 28.809340000152588},
    "Instances/inst-1300-0.2.txt": {"size": 1300, "type": 2, "time": 37.01651120185852},
    "Instances/inst-1100-0.3.txt": {"size": 1100, "type": 3, "time": 3520.974147081375},
    "Instances/inst-1400-0.2.txt": {"size": 1400, "type": 2, "time": 42.89517092704773},
    "Instances/inst-1200-0.3.txt": {"size": 1200, "type": 3, "time": 40.024768114089966},
    "Instances/inst-1500-0.2.txt": {"size": 1500, "type": 2, "time": 53.80194091796875},
    "Instances/inst-1300-0.3.txt": {"size": 1300, "type": 3, "time": 51.35131216049194},
    "Instances/inst-1400-0.3.txt": {"size": 1400, "type": 3, "time": 62.957350730895996},
    "Instances/inst-1500-0.3.txt": {"size": 1500, "type": 3, "time": 12507.26258301735},
}



def build_graph(data, type):
    sizes = []
    times = []

    for key, value in data.items():
        if value['type'] == type:
            sizes.append(value['size'] / 100)
            times.append(value['time'])

    plt.plot(times, sizes, marker='o')
    plt.ylabel("Taille des instances de type {} (×100)".format(type))
    plt.xlabel('Temps de résolution (en secondes)')
    plt.title('Chemin augmentant: taille des instances = f(temps de résolution)')
    plt.show()


build_graph(data, 1)
build_graph(data, 2)
build_graph(data, 3)

