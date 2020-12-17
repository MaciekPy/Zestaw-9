class Node:
    """Klasa reprezentująca węzeł drzewa binarnego."""

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)


def count_leafs(top):
    leafs = 0

    if top.left != None:
        leafs += count_leafs(top.left)
    else:
        return 1

    if top.right != None:
        leafs += count_leafs(top.right)
    else:
        return 1

    return leafs


def count_total(top):
    if top == None:
        return 0
    else:
        return top.data + count_total(top.right) + count_total(top.left)


tree = Node(5)
tree.left = Node(3)
tree.left.left = Node(6)
tree.left.right = Node(9)
tree.right = Node(7)
tree.right.right = Node(8)

print(count_leafs(tree))
print(count_total(tree))
