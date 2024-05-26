import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def add_edges_from_heap(graph, heap, pos, index=0, x=0, y=0, layer=1):
    if index < len(heap):
        node = heap[index]
        graph.add_node(node.id, color=node.color, label=node.val)
        if 2 * index + 1 < len(heap):
            left_child = heap[2 * index + 1]
            graph.add_edge(node.id, left_child.id)
            l = x - 1 / 2 ** layer
            pos[left_child.id] = (l, y - 1)
            add_edges_from_heap(graph, heap, pos, index=2 * index + 1, x=l, y=y - 1, layer=layer + 1)
        if 2 * index + 2 < len(heap):
            right_child = heap[2 * index + 2]
            graph.add_edge(node.id, right_child.id)
            r = x + 1 / 2 ** layer
            pos[right_child.id] = (r, y - 1)
            add_edges_from_heap(graph, heap, pos, index=2 * index + 2, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_heap(heap):
    tree = nx.DiGraph()
    pos = {heap[0].id: (0, 0)}
    tree = add_edges_from_heap(tree, heap, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

# Створення бінарної купи (як масиву вузлів)
heap = [Node(0), Node(1), Node(4), Node(5), Node(10), Node(3)]

# Відображення бінарної купи
draw_heap(heap)
