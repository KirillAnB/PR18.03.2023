import networkx as nx
import matplotlib.pyplot as plt


def dijkstra_stair(g):
    """Метод ищет кртачайший путь алгоритмом Дейкстры"""

    visited_nodes = {node: False for node in g.nodes}
    total_cost = {node: float("inf") for node in g.nodes}
    current_node = 0
    total_cost[current_node] = 0

    for _ in range(len(g)):
        not_visited_total_cost = {node: cost for node, cost in total_cost.items() if not visited_nodes[node]}
        min_cost = float("inf")
        for node, cost in not_visited_total_cost.items():
            if cost < min_cost:
                min_cost = cost
                current_node = node

        visited_nodes[current_node] = True
        for neighbor in g[current_node]:
            weight = g[current_node][neighbor]['weight']
            total_cost[neighbor] = min(total_cost[neighbor], total_cost[current_node] + weight)

    return total_cost


def graph_from_stair(expensive_stair):
    """Метод создает граф из последовательности"""
    list_of_nodes = [i for i in range(len(expensive_stair)+1)]
    graph = nx.DiGraph()
    graph.add_nodes_from(list_of_nodes)
    for i in range(len(list_of_nodes)-2):
        graph.add_weighted_edges_from([(list_of_nodes[i], list_of_nodes[i+1], expensive_stair[i]),
                                       (list_of_nodes[i], list_of_nodes[i+2], expensive_stair[i+1])
                                       ])
    """'костыль' для добавления последней связи"""
    graph.add_weighted_edges_from([(list_of_nodes[len(list_of_nodes)-2], list_of_nodes[-1], expensive_stair[-1])])
    return graph


if __name__ == '__main__':
    stairway = (5, 11, 43, 2,)

    # Создаем граф stairway_graph через функцию graph_from_stair:

    stairway_graph = graph_from_stair(stairway)

    # Создаем граф graph_2 и добавляем в него вершины и связи библиотекой networkx:
    graph_2 = nx.DiGraph()
    graph_2.add_weighted_edges_from([
        (0, 1, 5),
        (0, 2, 11),
        (1, 2, 11),
        (1, 3, 43),
        (2, 3, 43),
        (2, 4, 2),
        (3, 4, 2)
    ])
    # выводим всвязи графов для сравнения:
    print(stairway_graph.edges)
    print(graph_2.edges)
    # Считаем стоимость пути графа stairway_graph через функцию  dijkstra_stair из практического задания:
    print(dijkstra_stair(stairway_graph))
    # Считаем стоимость для graph_2 методом dijkstra_path_length библиотеки networkx(из узла 0 в узел 4):
    print(nx.dijkstra_path_length(graph_2, 0, 4))
    nx.draw_spring(stairway_graph, with_labels=True)
    plt.show()