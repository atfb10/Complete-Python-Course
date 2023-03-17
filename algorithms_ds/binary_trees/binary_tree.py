from node import Node 

class BinaryTree:
    def __init__(self, head: Node):
        self.head = head
    
    def add(self, new_node: Node) -> None:
        current_node = self.head
        while current_node:
            if new_node.value == current_node.value:
                raise ValueError('New Node value equals existing node value')
            elif new_node.value < current_node.value:
                if current_node.left:
                    current_node = current_node.left
                else:
                    current_node.left = new_node
                    break
            elif new_node.value > current_node.value:
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = new_node
                    break
        if not current_node:
            raise ValueError('Binary tree object\' head object is equal to None')
    
    def find(self, value: int) -> Node:
        current_node = self.head
        while current_node:
            if current_node.value == value:
                return current_node
            elif value < current_node.value:
                if current_node.left:
                    current_node = current_node.left
                else:
                    raise LookupError(f'Value {value} you are searching for does not exist in the tree object')
            elif value > current_node.value:
                if current_node.right:
                    current_node = current_node.right
                else:
                    raise LookupError(f'Value {value} you are searching for does not exist in the tree object')
        if not current_node:
            raise LookupError('Binary tree object\'s head object is equal to None')
    
    def print_inorder(self):
        self._inorder_recursive(self.head)

    '''
    recursive method. recursion is when a function calls itself
    '''
    def _inorder_recursive(self, current_node):
        '''
        method checks if current node is none. If so, it exits the function
        Otherwise, it calls itself for the left node
        '''
        if not current_node:
            return
        self._inorder_recursive(current_node=current_node.left)
        print(current_node)
        self._inorder_recursive(current_node=current_node.right)

    def print_preorder(self):
        self._preorder_recursive(self.head)
    
    def _preorder_recursive(self, current_node):
        if current_node is None:
            return
        print(current_node)
        self._preorder_recursive(current_node.left)
        self._preorder_recursive(current_node.right)

    def print_postorder(self):
        self._postorder_recursive(self.head)
    
    def _postorder_recursive(self, current_node):
        if not current_node:
            return
        self._postorder_recursive(current_node.left)
        self._postorder_recursive(current_node.right)
        print(current_node)

    def find_parent(self, value: int) -> Node:
        if not self.find(value):
            raise LookupError(f'Node with value of \'{value}\' does not exist in the tree object')
        
        current_node = self.head

        if current_node.value == value:
            return current_node
        
        while current_node:
            if (value < current_node.value and current_node.left.value == value) or (value > current_node.value and current_node.right.value == value):
                return current_node
            elif value < current_node.value:
                current_node = current_node.left
            elif value > current_node.value:
                current_node = current_node.right
        raise LookupError('Tree object\'s head value is None')

    def find_rightmost(self, node: Node) -> Node:
        current_node = node
        if not current_node:
            raise LookupError(f'Node \'{node}\' does not exist in the tree object')
 
        while current_node:
            if current_node.right is None:
                break
            else:
                current_node = current_node.right

        return current_node

    def delete(self, value: int) -> None:
        node_to_delete = self.find(value)
        node_to_delete_parent = self.find_parent(value)

        if not node_to_delete or not node_to_delete_parent:
            raise LookupError(f'Node with value of <{value}> does not exist in binary tree object')

        # 0 children
        if node_to_delete.left is None and node_to_delete.right is None:
            if node_to_delete == node_to_delete_parent.left:
                node_to_delete_parent.left = None
            elif node_to_delete == node_to_delete_parent.right:
                node_to_delete_parent.right = None
            elif node_to_delete == node_to_delete_parent:
                self.delete_whole_tree()

        # 1 child
        elif node_to_delete.left or node_to_delete.right:
            if node_to_delete == node_to_delete_parent.left:
                node_to_delete_parent.left == node_to_delete.left or node_to_delete.right
            elif node_to_delete == node_to_delete_parent.right:
                node_to_delete_parent.right = node_to_delete.left or node_to_delete.right
            elif node_to_delete == node_to_delete_parent:
                self.head = self.set_head(node_to_delete.left or node_to_delete.right)

        # 2 children
        else:
            rightmost = self.find_rightmost(node_to_delete.left)
            rightmost_parent = self.find_parent(rightmost.value)

            if rightmost_parent != node_to_delete:
                    rightmost_parent.right = rightmost.left
                    rightmost.left = node_to_delete.left
            
            rightmost.right = node_to_delete.right

            if node_to_delete == node_to_delete_parent.left:
                node_to_delete_parent.left = rightmost
            elif node_to_delete == node_to_delete_parent.right:
                node_to_delete_parent.right = rightmost
            else:
                self.set_head(rightmost)
        return
    
    def delete_whole_tree(self) -> None:
        self.head = None
        return
    
    def set_head(self, new_head: Node) -> None:
        self.head = new_head
        return