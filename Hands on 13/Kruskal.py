MAX_NODES = 30
class Edge:
    def __init__(self, u, v, w):
        self.u = u  
        self.v = v  
        self.w = w 

class EdgeList:
    def __init__(self):
        self.data = [] 
        self.n = 0      

adjacency_matrix = [
    [0, 4, 0, 0, 0, 0, 0, 8, 0],
    [4, 0, 8, 0, 0, 0, 0, 11, 0],
    [0, 8, 0, 7, 0, 4, 0, 0, 2],
    [0, 0, 7, 0, 9, 14, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0],
    [0, 0, 4, 14, 10, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6],
    [8, 0, 0, 0, 0, 0, 1, 0, 7],
    [0, 0, 2, 0, 0, 0, 6, 7, 0]
]

n = 9

parent = [i for i in range(MAX_NODES)]

vertices = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

elist = EdgeList()

def kruskal():
    global elist
    elist.n = 0

    for i in range(n):
        for j in range(n):
            if adjacency_matrix[i][j] != 0:
                elist.data.append(Edge(i, j, adjacency_matrix[i][j]))
                elist.n += 1

    elist.data.sort(key=lambda x: x.w)
    print("\nEdges of Minimum Cost Spanning Tree are")
    for i in range(elist.n):
        u = find(elist.data[i].u)
        v = find(elist.data[i].v)

        if u != v:
            union(u, v)
            print(f"{vertices[elist.data[i].u]} -> {vertices[elist.data[i].v]} = {elist.data[i].w}")

def find(i):
    while parent[i] != i:
        i = parent[i]
    return i

def union(i, j):
    parent[i] = j

if __name__ == "__main__":
    kruskal()

------------------------OUTPUT-----------------------
Edges of Minimum Cost Spanning Tree are
g -> h = 1
c -> i = 2
f -> g = 2
a -> b = 4
c -> f = 4
c -> d = 7
a -> h = 8
d -> e = 9

Process finished with exit code 0
