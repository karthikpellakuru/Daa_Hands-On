class Side:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight

class Node:
    def __init__(self, value):
        self.value = value
        self.distance = float('inf')
        self.predecessor = None

def update_distance(source, destination, weight):
    if destination.distance > source.distance + weight:
        destination.distance = source.distance + weight
        destination.predecessor = source

def initialize_graph(graph, start):
    for node in graph.nodes:
        node.distance = float('inf')
        node.predecessor = None
    start.distance = 0

def explore_graph(graph, start):
    initialize_graph(graph, start)
    for i in range(len(graph.nodes) - 1):
        for (source, destination) in graph.weights.keys():
            update_distance(source, destination, graph.weights[(source, destination)])
    for (source, destination) in graph.weights.keys():
        if destination.distance > source.distance + graph.weights[(source, destination)]:
            return False
    return True

class Network:
    def __init__(self, nodes):
        self.nodes = nodes
        self.connections = {}
        self.weights = {}
        for node in nodes:
            self.connections[node] = []

    def add_link(self, source, destination, weight):
        if source not in self.connections.keys():
            self.connections[source] = [destination]
        else:
            self.connections[source].append(destination)
        self.weights[(source, destination)] = weight

    def __str__(self):
        print("\n ---Connected Nodes ---")
        for node in self.connections.keys():
            print(node.value, end=": ")
            for neighbor in self.connections[node]:
                print(neighbor.value, end=" ")
            print("\b")
        return "---End of Connected Nodes ---\n"


if __name__ == "__main__":
    # Example from figure 24.4 of Chapter 24 of 2009 Introduction to Algorithms by Cormen et al.
    # s: 0, t: 1, x: 2, y: 3, z: 4

    nodes = [Node(i) for i in range(5)]

    connections = [Side(nodes[0], nodes[1], 6),
                   Side(nodes[0], nodes[3], 7),
                   Side(nodes[1], nodes[2], 5),
                   Side(nodes[1], nodes[3], 8),
                   Side(nodes[1], nodes[4], -4),
                   Side(nodes[2], nodes[1], -2),
                   Side(nodes[3], nodes[2], -3),
                   Side(nodes[3], nodes[4], 9),
                   Side(nodes[4], nodes[0], 2),
                   Side(nodes[4], nodes[2], 7)]

    network = Network(nodes)
    for connection in connections:
        network.add_link(connection.source, connection.destination, connection.weight)
    for key in network.weights.keys():
        print(key, network.weights[key])
    print(len(network.weights.keys()))
    print(explore_graph(network, nodes[0]))
