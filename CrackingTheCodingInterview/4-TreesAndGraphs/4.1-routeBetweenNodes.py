# Given a directed graph and two nodes (s and e), design an algorithm to find out whether there is a route from s to e.

class QueueNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        node = QueueNode(data)
        if not self.head:
            self.head = node
        if self.tail:
            self.tail.next = node
        self.tail = node

    def dequeue(self):
        if self.head:
            data = self.head.data
            self.head = self.head.next
            return data
        return None

    def is_empty(self):
        return self.head is None

class Node:
    def __init__(self, data, neighbors):
        self.data = data
        self.neighbors = neighbors
        self.visited = False

class Graph:
    def __init__(self, nodes):
        self.nodes = nodes

# time: O(V+E), space: O(V)
def routeBetweenNodes(graph, s, e):
    # BFS will find the shortest path first

    queue = Queue()
    s.visited = True
    queue.enqueue(s)

    while not queue.is_empty():
        r = queue.dequeue()
        if r == e:
            return True
        for neighbor in r.neighbors:
            node = graph.nodes[neighbor]
            if not node.visited:
                node.visited = True
                queue.enqueue(node)
    
    return False

graph = Graph([
    Node('A', [1, 2, 3]),
    Node('B', [2]),
    Node('C', [3]),
    Node('D', [2, 4]),
    Node('E', [3]),
    Node('E', [1, 2, 3, 4]),
])

print(routeBetweenNodes(graph, graph.nodes[0], graph.nodes[4])) # True
print(routeBetweenNodes(graph, graph.nodes[0], graph.nodes[5])) # False
