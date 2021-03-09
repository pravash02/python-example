"""
For a given value, Find the closest value in BST

Binary Search Tree:
         9
       /   \
      4      17
     / \      \
    3   6      22
       / \     /
      5   7   20

    target: 18

Output 17

"""


class Newnode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def getClosestValue(root, tgt_val, MIN_VAL, prev_root):
    if root == None:
        print('MIN_VAL in BST =', prev_root)
        return prev_root

    if root.val == tgt_val:
        print('comparing MIN_VAL with target_val', root.val)
        return root.val

    if MIN_VAL > abs(root.val - tgt_val):
        MIN_VAL = abs(root.val - tgt_val)
        prev_root = root.val
        # print('setting MIN_VAL inside if', (MIN_VAL, prev_root))

    if tgt_val > root.val:
        getClosestValue(root.right, tgt_val, MIN_VAL, prev_root)

    else:
        getClosestValue(root.left, tgt_val, MIN_VAL, prev_root)


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

    MIN_VAL = float('inf')
    target_val = 12
    getClosestValue(root, target_val, MIN_VAL, prev_root=None)
