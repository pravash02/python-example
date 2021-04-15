"""
In-Order traversal using recursive and iterative

"""


class Newnode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

    def printIterative(self, root):
        lst = []
        ord = []
        current = root

        while True:
            if current is not None:
                lst.append(current)
                current = current.left
            elif lst:
                current = lst.pop()
                ord.append(str(current.val))
                current = current.right
            else:
                break

        return ord

    def printRecursive(self, root, traversal):
        if root:
            traversal = self.printRecursive(root.left, traversal)
            traversal += str(root.val) + '->'
            traversal = self.printRecursive(root.right, traversal)
        return traversal


if __name__ == '__main__':
    root = Newnode(9)
    root.left = Newnode(4)
    root.right = Newnode(17)
    root.left.left = Newnode(3)
    root.left.right = Newnode(6)
    root.left.right.left = Newnode(5)
    root.left.right.right = Newnode(7)
    root.right.right = Newnode(22)
    root.right.right.left = Newnode(20)

    print(root.printRecursive(root, traversal=''))
    print('->'.join(root.printIterative(root)))
