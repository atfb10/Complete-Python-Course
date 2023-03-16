from binary_tree import BinaryTree
from node import Node

head = Node(10)

tree = BinaryTree(head)
tree.add(Node(11))
tree.add(Node(2))
tree.add(Node(9))
tree.add(Node(12))
tree.add(Node(21))
tree.add(Node(81))
tree.add(Node(1))

print(tree.head)
print(tree.head.left)
print(tree.head.right)
print()

tree.print_inorder()
print()

tree.print_preorder()
print()

tree.print_postorder()