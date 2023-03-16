class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        return f'Node <{self.value}>'