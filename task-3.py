import heapq

class Graph:
    def __init__(self):
        self.edges = {}
        self.vertices = set()
    
    def add_edge(self, from_node, to_node, weight):
        if from_node not in self.edges:
            self.edges[from_node] = []
        self.edges[from_node].append((to_node, weight))
        
        # Додаємо вершини до множини
        self.vertices.add(from_node)
        self.vertices.add(to_node)
        
    def dijkstra(self, start):
        # Ініціалізація
        queue = []
        heapq.heappush(queue, (0, start))  # (відстань, вершина)
        distances = {vertex: float('infinity') for vertex in self.vertices}
        distances[start] = 0
        
        while queue:
            current_distance, current_vertex = heapq.heappop(queue)
            
            # Якщо знайдена відстань до вершини більша, ніж поточна, ігноруємо її
            if current_distance > distances[current_vertex]:
                continue
                
            # Оновлюємо відстані до сусідів
            for neighbor, weight in self.edges.get(current_vertex, []):
                distance = current_distance + weight
                
                # Якщо знайшли коротший шлях до сусіда
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(queue, (distance, neighbor))
                    
        return distances

# Приклад використання:
g = Graph()
g.add_edge('A', 'B', 1)
g.add_edge('A', 'C', 4)
g.add_edge('B', 'C', 2)
g.add_edge('B', 'D', 5)
g.add_edge('C', 'D', 1)

distances = g.dijkstra('A')
print(distances)  # Виведе найкоротші відстані від 'A' до всіх інших вершин
