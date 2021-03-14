"""
Finding the branch sum of a tree

"""


class Newnode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

    def printBranchSumIterative(self, root):
        pass

    def printBranchSumRecursive(self, root, s, sum_list):
        if root is None:
            return

        s += root.val
        self.printBranchSumRecursive(root.left, s, sum_list)
        self.printBranchSumRecursive(root.right, s, sum_list)
        if root.left is None and root.right is None:
            sum_list.append(s)
        return sum_list


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

    print(root.printBranchSumRecursive(root, s=0, sum_list=[]))
    print(root.printBranchSumIterative(root))
