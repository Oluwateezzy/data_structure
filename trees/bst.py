class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert_recursive(current_node.left, value)
        else:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert_recursive(current_node.right, value)

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, current_node, value):
        if current_node is None:
            return False
        if value == current_node.value:
            return True
        elif value < current_node.value:
            return self._search_recursive(current_node.left, value)
        else:
            return self._search_recursive(current_node.right, value)

    def in_order_traversal(self):
        return self._in_order_recursive(self.root, [])

    def _in_order_recursive(self, node, result):
        if node:
            self._in_order_recursive(node.left, result)
            result.append(node.value)
            self._in_order_recursive(node.right, result)
        return result

    def pre_order_traversal(self):
        return self._pre_order_recursive(self.root, [])

    def _pre_order_recursive(self, node, result):
        if node:
            result.append(node.value)
            self._pre_order_recursive(node.left, result)
            self._pre_order_recursive(node.right, result)
        return result

    def post_order_traversal(self):
        return self._post_order_recursive(self.root, [])

    def _post_order_recursive(self, node, result):
        if node:
            self._post_order_recursive(node.left, result)
            self._post_order_recursive(node.right, result)
            result.append(node.value)
        return result


bst = BinarySearchTree()
values = [8, 3, 10, 1, 6, 14, 4, 7, 13]

for value in values:
    bst.insert(value)
print("In-order Traversal (Sorted):", bst.in_order_traversal())
print("Pre-order Traversal:", bst.pre_order_traversal())
print("Post-order Traversal:", bst.post_order_traversal())

search_value = 6
print(f"Is {search_value} in the tree?", bst.search(search_value))
