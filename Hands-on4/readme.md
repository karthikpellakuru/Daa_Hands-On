2 Prove the time complexity of the algorithms.

Ans. In the original Fibonacci implementation, each call to fib(n) results in two additional recursive calls, leading to a branching tree structure. At each level of the recursion, there are two child nodes, representing the two recursive calls made at that level. This binary tree-like structure results in an exponential growth of function calls.

The number of function calls at each level follows a power of 2 pattern. Specifically, there are 2^n function calls at level n. Therefore, the total number of function calls in the recursive tree is proportional to 2^n.

Expressed in big-O notation, the time complexity is O(2^n), indicating that the time required by the algorithm grows exponentially with the input size n. This exponential growth leads to inefficiency for larger values of n due to the vast number of redundant calculations.

3 Comment on way's you could improve your implementation.

Ans. The primary limitation of the original Fibonacci implementation lies in its inefficiency for larger values of n due to its exponential time complexity. In this implementation, the number of recursive calls grows rapidly, resulting in a branching tree structure that leads to redundant calculations.

To address this inefficiency, optimization techniques like memoization or dynamic programming can be employed. These approaches involve storing and reusing previously computed results to avoid redundant calculations. In the context of Fibonacci, memoization typically utilizes a data structure, such as a dictionary or an array, to store intermediate results, reducing the need to recompute Fibonacci values for the same inputs.

Memoization and dynamic programming can significantly enhance the efficiency of the algorithm, bringing the time complexity down to O(n) by eliminating redundant calculations. This improvement makes the algorithm more scalable and suitable for larger inputs.
