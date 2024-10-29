class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if not node.left:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if not node.right:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)

    def search(self, value):
        return self._search_tree(self.root, value)

    def _search_tree(self, node, value):
        if not node:
            return False
        if node.value == value:
            return True
        elif value < node.value:
            return self._search_tree(node.left, value)
        else:
            return self._search_tree(node.right, value)


class RedBlackTree:
    RED = True
    BLACK = False

    class Node:
        def __init__(self, value, color=True):
            self.value = value
            self.color = color
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(self.root, value)
        self.root.color = self.BLACK  # Ensure root is black

    def _insert(self, node, value):
        if node is None:
            return self.Node(value)

        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)

        if self._is_red_color(node.right) and not self._is_red_color(node.left):
            node = self._r_rotate(node)
        if self._is_red_color(node.left) and self._is_red_color(node.left.left):
            node = self._l_rotate(node)
        if self._is_red_color(node.left) and self._is_red_color(node.right):
            self._change_colors(node)

        return node

    def _is_red_color(self, node):
        return node is not None and node.color == self.RED

    def _l_rotate(self, node):
        x = node.right
        node.right = x.left
        x.left = node
        x.color = node.color
        node.color = self.RED
        return x

    def _r_rotate(self, node):
        x = node.left
        node.left = x.right
        x.right = node
        x.color = node.color
        node.color = self.RED
        return x

    def _change_colors(self, node):
        node.color = not node.color
        node.left.color = not node.left.color
        node.right.color = not node.right.color

    def search(self, value):
        return self._search_tree(self.root, value)

    def _search_tree(self, node, value):
        if not node:
            return False
        if node.value == value:
            return True
        elif value < node.value:
            return self._search_tree(node.left, value)
        else:
            return self._search_tree(node.right, value)


class AVLTree:
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None
            self.height = 1

    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if not node:
            return self.Node(value)
        if value < node.value:
            node.left = self._insert(node.left, value)
        else:
            node.right = self._insert(node.right, value)

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

        balance = self._get_balance(node)

        # Left Left Case
        if balance > 1 and value < node.left.value:
            return self._r_rotate(node)

        # Right Right Case
        if balance < -1 and value > node.right.value:
            return self._l_rotate(node)

        # Left Right Case
        if balance > 1 and value > node.left.value:
            node.left = self._l_rotate(node.left)
            return self._r_rotate(node)

        # Right Left Case
        if balance < -1 and value < node.right.value:
            node.right = self._r_rotate(node.right)
            return self._l_rotate(node)

        return node

    def _get_height(self, node):
        if not node:
            return 0
        return node.height

    def _get_balance(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _l_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _r_rotate(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))

        return x

    def search(self, value):
        return self._search_tree(self.root, value)

    def _search_tree(self, node, value):
        if not node:
            return False
        if node.value == value:
            return True
        elif value < node.value:
            return self._search_tree(node.left, value)
        else:
            return self._search_tree(node.right, value)


# Tests for Binary Search Tree
bst = BinarySearchTree()
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)
bst.insert(4)
bst.insert(6)
bst.insert(8)

print("Binary Search Tree:")
print(bst.search(5))  # Output: True
print(bst.search(10))  # Output: False

# Tests for Red-Black Tree
rbt = RedBlackTree()
rbt.insert(5)
rbt.insert(3)
rbt.insert(7)
rbt.insert(2)
rbt.insert(4)
rbt.insert(6)
rbt.insert(8)

print("\nRed-Black Tree:")
print(rbt.search(5))  # Output: True
print(rbt.search(10))  # Output: False

# Tests for AVL Tree
avl = AVLTree()
avl.insert(5)
avl.insert(3)
avl.insert(7)
avl.insert(2)
avl.insert(4)
avl.insert(6)
avl.insert(8)

print("\nAVL Tree:")
print(avl.search(5))  # Output: True
print(avl.search(10))  # Output: False
