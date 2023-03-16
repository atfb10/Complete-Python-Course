new_node = None(value=5, left=None, right=None)
head = self.head

# Add element
while head:
    if new_node.value == head.value:
        print('New Node value = to existing value in the tree. No duplicates allowed')
        break
    elif new_node.value < head.value:
        if head.left:
            head = head.left
        else:
            head.left = new_node
            break
    elif: new_node.value > head.value:
        if head.right:
            head = head.right
        else:
            head.right = new_node
            break