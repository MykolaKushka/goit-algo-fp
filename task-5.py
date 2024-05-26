import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, traversal_type="DFS"):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    if traversal_type == "DFS":
        order = dfs_traversal(tree_root)
    else:
        order = bfs_traversal(tree_root)

    apply_colors(tree, order)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def dfs_traversal(root):
    stack = [root]
    order = []
    visited = set()

    while stack:
        node = stack.pop()
        if node.id not in visited:
            visited.add(node.id)
            order.append(node)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
    return order

def bfs_traversal(root):
    queue = deque([root])
    order = []
    visited = set()

    while queue:
        node = queue.popleft()
        if node.id not in visited:
            visited.add(node.id)
            order.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return order

def apply_colors(graph, order):
    n = len(order)
    for i, node in enumerate(order):
        intensity = 255 - int(255 * (i / (n - 1)))  # Від темного до світлого
        hex_color = f'#{intensity:02x}{intensity:02x}ff'  # Відтінки синього
        node.color = hex_color
        graph.nodes[node.id]['color'] = hex_color

# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Відображення обходу в глибину
draw_tree(root, traversal_type="DFS")

# Відображення обходу в ширину
draw_tree(root, traversal_type="BFS")
