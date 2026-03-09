import math

# Alpha-Beta Pruning Implementation
# Alpha-beta pruning is an optimization technique for the minimax algorithm that reduces the 
# number of nodes evaluated by the minimax algorithm in its search tree.

def alpha_beta_pruning(depth, node_index, is_maximizing, values, alpha, beta):
    """
    Minimax with Alpha-Beta Pruning.
    
    :param depth: Current depth in the game tree
    :param node_index: Index of the current node in the leaf values list
    :param is_maximizing: True if current node is MAX, False if MIN
    :param values: List containing the values of the leaf nodes
    :param alpha: Current alpha value (best value found for MAX)
    :param beta: Current beta value (best value found for MIN)
    :return: The optimal value for the root node
    """
    
    # Base case: Leaf node (assuming a full binary tree of depth 3)
    if depth == 3:
        return values[node_index]

    if is_maximizing:
        best = -math.inf
        # Recur for children (assuming binary tree for simplicity)
        for i in range(2):
            val = alpha_beta_pruning(depth + 1, node_index * 2 + i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            
            # Pruning condition
            if beta <= alpha:
                print(f"Pruning at depth {depth}, node {node_index}")
                break
        return best
    else:
        best = math.inf
        # Recur for children
        for i in range(2):
            val = alpha_beta_pruning(depth + 1, node_index * 2 + i, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            
            # Pruning condition
            if beta <= alpha:
                print(f"Pruning at depth {depth}, node {node_index}")
                break
        return best

if __name__ == "__main__":
    # Example leaf node values (8 values for depth 3 binary tree)
    # The tree looks like this:
    #             Root
    #          /        \
    #       MAX          MAX
    #     /    \       /    \
    #   MIN    MIN   MIN    MIN
    #  / \    / \   / \    / \
    # 3   5  6   9 1   2  0  -1
    
    leaf_values = [3, 5, 6, 9, 1, 2, 0, -1]
    
    print("Leaf Node Values:", leaf_values)
    optimal_val = alpha_beta_pruning(0, 0, True, leaf_values, -math.inf, math.inf)
    print("The optimal value from Alpha-Beta Pruning is:", optimal_val)
