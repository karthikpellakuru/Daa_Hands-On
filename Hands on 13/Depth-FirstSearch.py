def depth_first_search(node_index, adjacency_matrix, visited_nodes, node_names):
    
    print(node_names[node_index], end=" ")
    
    visited_nodes[node_index] = 1

    
    for adjacent_node_index in range(len(adjacency_matrix)):
        
        if not visited_nodes[adjacent_node_index] and adjacency_matrix[node_index][adjacent_node_index] == 1:
            
            depth_first_search(adjacent_node_index, adjacency_matrix, visited_nodes, node_names)


def main():
    
    MAX_NODES = 9
    
    adjacency_matrix = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],  
        [0, 0, 1, 1, 0, 0, 0, 0, 0],  
        [0, 0, 0, 0, 0, 0, 0, 0, 1], 
        [0, 0, 0, 0, 0, 0, 0, 0, 1],  
        [0, 0, 0, 1, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 1, 0, 0, 1, 0],  
        [0, 0, 0, 0, 0, 0, 0, 1, 0],  
        [0, 0, 0, 0, 0, 0, 0, 0, 0],  
        [0, 0, 0, 0, 0, 0, 0, 0, 0]  
    ]

    visited_nodes = [0] * MAX_NODES
  
    node_names = ["watch", "shirt", "tie", "belt", "pants", "undershorts", "socks", "shoes", "jacket"]

    print("DFS traversal of the graph is: ", end="")
 
    for node_index in range(MAX_NODES):
        if not visited_nodes[node_index]:
            depth_first_search(node_index, adjacency_matrix, visited_nodes, node_names)

if __name__ == "__main__":
    main()
  
----------OUTPUT---------
DFS traversal of the graph is: watch shirt tie jacket belt pants undershorts shoes socks 
Process finished with exit code 0
