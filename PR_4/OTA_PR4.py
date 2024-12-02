import heapq
import networkx as nx
import matplotlib.pyplot as plt

def dijkstra(graph, start, end):
    """
    Реализация алгоритма Дейкстры для поиска кратчайшего пути в графе.

    :param graph: Словарь, представляющий граф, где ключи - вершины, а значения - словари с соседями и весами ребер.
    :param start: Начальная вершина.
    :param end: Конечная вершина.
    :return: Кортеж, содержащий кратчайшее расстояние и список вершин кратчайшего пути.
    """
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    previous_vertices = {vertex: None for vertex in graph}
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        if current_vertex == end:
            break
        
        if current_distance > distances[current_vertex]:
            continue
        
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                previous_vertices[neighbor] = current_vertex
    
    path, current_vertex = [], end
    while current_vertex is not None:
        path.append(current_vertex)
        current_vertex = previous_vertices[current_vertex]
    
    path.reverse()
    return distances[end], path

def draw_graph(graph, start_node, end_node, shortest_path=None):
    """
    Визуализация графа с использованием библиотеки NetworkX и Matplotlib.

    :param graph: Словарь, представляющий граф.
    :param start_node: Начальная вершина.
    :param end_node: Конечная вершина.
    :param shortest_path: Список вершин кратчайшего пути (опционально).
    """
    G = nx.DiGraph()
    
    for node, neighbors in graph.items():
        for neighbor, weight in neighbors.items():
            G.add_edge(node, neighbor, weight=weight)
    
    pos = nx.spring_layout(G)
    
    nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=700, edgecolors='black')
    nx.draw_networkx_edges(G, pos, edge_color='gray', width=2.5)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', font_size=14, label_pos=0.5)
    nx.draw_networkx_labels(G, pos, font_size=16, font_weight='bold')
    
    if shortest_path:
        shortest_path_edges = [(shortest_path[i], shortest_path[i+1]) for i in range(len(shortest_path)-1)]
        nx.draw_networkx_edges(G, pos, edgelist=shortest_path_edges, edge_color='green', width=4)
    
    plt.axis('off')
    plt.show()

graph1 = {
    'A': {'B': 5, 'D': 8, 'E': 7},
    'B': {'C': 6, 'D': 2},
    'C': {'G': 8},
    'D': {'G': 7, 'F': 2},
    'E': {'F': 4},
    'F': {'G': 2},
    'G': {}
}

graph2 = {
    0: {1: 5, 4: 9, 7: 8},
    1: {7: 4, 2: 12, 3: 15},
    2: {3: 3, 6: 11},
    3: {6: 9},
    4: {7: 5, 5: 4, 6: 20},
    5: {2: 1, 6: 13},
    6: {},
    7: {2: 7, 5: 6}
}

def main():
    """
    Основная функция для выбора графа и поиска кратчайшего пути с последующей визуализацией.
    """
    print("Выберите граф для поиска кратчайшего пути:")
    print("1. Граф 1")
    print("2. Граф 2")
    
    choice = input("Введите номер графа: ")
    
    if choice == '1':
        start_node = 'A'
        end_node = 'G'
        graph = graph1
    elif choice == '2':
        start_node = 0
        end_node = 6
        graph = graph2
    else:
        print("Неверный выбор.")
        return
    
    shortest_distance, shortest_path = dijkstra(graph, start_node, end_node)
    print(f"Кратчайшее расстояние: {shortest_distance}")
    print(f"Кратчайший путь: {shortest_path}")
    
    draw_graph(graph, start_node, end_node, shortest_path)

if __name__ == "__main__":
    main()