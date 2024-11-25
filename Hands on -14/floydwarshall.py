from typing import List

import numpy as np

def floyd_warshall_algorithm(W: List[List[int]]):
    W_matrix = np.array(W)
    num_vertices = len(W_matrix)
    D_matrix = np.array([[[float(0) for _ in range(num_vertices)] for _ in range(num_vertices)] for _ in range(num_vertices)])
    D_matrix[0] = W_matrix
    for k in range(0, num_vertices - 1):
        k_plus_one = k + 1
        for i in range(0, num_vertices):
            for j in range(0, num_vertices):
                D_matrix[k_plus_one][i][j] = min(D_matrix[k_plus_one - 1][i][j], D_matrix[k_plus_one - 1][i][k] + D_matrix[k_plus_one - 1][k][j])

        print(f"\nD{k_plus_one}")
        print(D_matrix[k_plus_one])
    return D_matrix[num_vertices - 1]

# Floyd-Warshall algorithm implemented recursively
def floyd_warshall_recursive_algorithm(W: List[List[int]], k: int):
    num_vertices = len(W)
    D_k = [[float(0) for _ in range(num_vertices)] for _ in range(num_vertices)]
    D_k = np.array(D_k)
    for i in range(num_vertices):
        for j in range(num_vertices):
            D_k[i][j] = min(W[i][j], W[i][k] + W[k][j])
    if k == num_vertices - 1:
        return D_k
    print(f"\nD{k + 1}")
    print(D_k)
    return floyd_warshall_recursive_algorithm(D_k, k + 1)

def generate_parent_matrix(W: List[List[int]]):
    num_vertices = len(W)
    parent_matrix = [[float(0) for _ in range(num_vertices)] for _ in range(num_vertices)]
    parent_matrix = np.array(parent_matrix)
    for i in range(num_vertices):
        for j in range(num_vertices):
            if i != j and W[i][j] != float('inf'):
                parent_matrix[i][j] = i
            else:
                parent_matrix[i][j] = None
    return parent_matrix

if __name__ == "__main__":
    # Example from figure 25.4 of Chapter 25 of 2009 Introduction to Algorithms by Cormen et al.
    W_input = [[0, 3, 8, float('inf'), -4],
        [float('inf'), 0, float('inf'), 1, 7],
        [float('inf'), 4, 0, float('inf'), float('inf')],
        [2, float('inf'), -5, 0, float('inf')],
        [float('inf'), float('inf'), float('inf'), 6, 0]]

    W_input_matrix = np.array(W_input)
    print("\nSimple Floyd-Warshall Algorithm")
    print("\nFinal\n", floyd_warshall_algorithm(W_input))
    print("\nRecursive Floyd-Warshall Algorithm")
    print("\nFinal\n", floyd_warshall_recursive_algorithm(W_input_matrix, 0))

    print("\nParent Matrix")
    print(generate_parent_matrix(W_input))
