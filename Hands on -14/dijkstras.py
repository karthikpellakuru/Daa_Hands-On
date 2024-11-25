class Route:
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight

class Node:
    def __init__(self, data):
        self.data = data
        self.distance = float('inf')
        self.predecessor = None

def update_distance(start, end, weight):
    if end.distance > start.distance + weight:
        end.distance = start.distance + weight
        end.predecessor = start

def initialize_single_node(graph, start):
    for node in graph.nodes:
        node.distance = float('inf')
        node.predecessor = None
    start.distance = 0

def extract_minimum(Q):
    minimum = Q[0]
    for node in Q:
        if node.distance < minimum.distance:
            minimum = node
    Q.remove(minimum)
    return minimum

def find_shortest_paths(graph, start):
    initialize_single_node(graph, start)
    S = []
    Q = graph.nodes[:]
    while Q:
        current_node = extract_minimum(Q)
        S.append(current_node)
        for neighbor in graph.connections[current_node]:
            update_distance(current_node, neighbor, graph.weights[(current_node, neighbor)])
    return S

def retrieve_path(node):
    path = []
    while node:
        path.append(node.data)
        node = node.predecessor
    path.reverse()
    return path

class Network:
    def __init__(self, nodes):
        self.nodes = nodes
        self.connections = {}
        self.weights = {}
        for node in nodes:
            self.connections[node] = []

    def add_route(self, start, end, weight):
        if start not in self.connections.keys():
            self.connections[start] = [end]
        else:
            self.connections[start].append(end)
        self.weights[(start, end)] = weight

    def __str__(self):
        print("\n ---Connected Nodes ---")
        for node in self.connections.keys():
            print(node.data, end=": ")
            for neighbor in self.connections[node]:
                print(neighbor.data, end=" ")
            print("\b")
        return "---End of Connected Nodes ---\n"


if __name__ == "__main__":
    # Example from figure 24.6 of Chapter 24 of 2009 Introduction to Algorithms by Cormen et al.
    # s: 0, t: 1, x: 2, y: 3, z: 4

    nodes = [Node(i) for i in range(5)]

    routes = [Route(nodes[0], nodes[1], 10),
             Route(nodes[0], nodes[3], 5),
             Route(nodes[1], nodes[2], 1),
             Route(nodes[1], nodes[3], 2),
             Route(nodes[2], nodes[4], 4),
             Route(nodes[3], nodes[1], 3),
             Route(nodes[3], nodes[2], 9),
             Route(nodes[3], nodes[4], 2),
             Route(nodes[4], nodes[0], 7),
             Route(nodes[4], nodes[2], 6)]
    network = Network(nodes)
    for route in routes:
        network.add_route(route.start, route.end, route.weight)
    shortest_paths = find_shortest_paths(network, nodes[0])
    print("Node | Distance | Path")
    print("-----------------------")
    for node in shortest_paths:
        path = retrieve_path(node)
        print(f" {node.data}     | {node.distance}       | {'->'.join(map(str, path))}")
