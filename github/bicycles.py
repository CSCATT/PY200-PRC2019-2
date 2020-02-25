# задача. Можно ли обойтись одним велосипедом? Заказы даны в формате кортежей (час начала, час конца)

import networkx as nx
import matplotlib.pyplot as plt

orders = [
    (9, 12),
    (10, 12)
]

def plot(graph):
    pos = nx.spring_layout(graph) # словарь, в котором ключи это вершины и их координаты в спец. формате
    labels = {n: n for n in graph.nodes()} # против каждой вершины мы можем назвать их как-то, мы здесь ими же и назвали
    nx.draw_networkx_nodes(graph, pos) # отрисовывает вершины
    nx.draw_networkx_edges(graph, pos) # отрисовывает связи
    nx.draw_networkx_labels(graph, pos, labels, font_size=16) # отрисовывает лэйблы

    #plt.show() # визуализирует
    print(graph.degree)


if __name__ == "__main__":
    graph = nx.MultiDiGraph() # nx.MultiGraph() так как может сразу несколько связей идти из одного нода в другой
    graph.add_nodes_from(range(0, 24))  # часы

    for order in orders:
        for i in range(order[0], order[1]):
            graph.add_edge(i, i + 1)

    for d in graph.out_degree:
        print(d)