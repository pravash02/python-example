class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, val):
        self.items.insert(0, val)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1].value

    def __len__(self):
        self.size()

    def size(self):
        return len(self.items)


class Stack:
    def __init__(self):
        self.stack_lst = []

    def push(self, item):
        self.stack_lst.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack_lst.pop()

    def is_empty(self):
        return len(self.stack_lst) == 0

    def peek(self):
        return self.stack_lst[-1]


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(Stack):
    def __init__(self, root):
        Stack.__init__(self)
        self.root = Node(root)

    def traversal_type(self, traversal_type):
        if traversal_type == 'pre-order':
            return self.pre_order_print(bt.root, '')
        if traversal_type == 'in-order':
            return self.in_order_print(bt.root, '')
        if traversal_type == 'post-order':
            return self.post_order_print(bt.root, '')
        if traversal_type == 'level-order':
            return self.level_order_print(bt.root)
        if traversal_type == 'reverse-level-order':
            return self.reverse_level_order_print(bt.root)
        if traversal_type == 'bst-row-count-iterative':
            return self.binary_search_row_count_iterative(bt.root)
        if traversal_type == 'in-order-iterative':
            return self.in_order_print_iterative(bt.root)
        if traversal_type == 'level-maximum-nodes':
            return self.max_level_nodes(bt.root)

    def pre_order_print(self, start, traversal):
        # Root -> Left -> Right
        if start:
            traversal += (str(start.value) + "->")
            traversal = self.pre_order_print(start.left, traversal)
            traversal = self.pre_order_print(start.right, traversal)
        return traversal

    def in_order_print(self, start, traversal):
        # Left -> Root -> Right
        if start:
            traversal = self.in_order_print(start.left, traversal)
            traversal += (str(start.value) + "->")
            traversal = self.in_order_print(start.right, traversal)
        return traversal

    def post_order_print(self, start, traversal):
        # Left -> Right -> Root
        if start:
            traversal = self.post_order_print(start.left, traversal)
            traversal = self.post_order_print(start.right, traversal)
            traversal += (str(start.value) + "->")
        return traversal

    def binary_search_row_count_iterative(self, root):
        if root is None:
            return 0
        lst = []
        count = 0
        self.push(root)

        while not self.is_empty():
            root = self.pop()
            if root.left is not None:
                self.push(root.left)
            if root.left is not None and root.right is not None:
                count += 1
            if root.right is not None:
                self.push(root.right)

        return count

    @staticmethod
    def in_order_print_iterative(root):
        lst = []
        res = []
        current = root

        while True:
            if current is not None:
                lst.append(current)
                current = current.left
            elif lst:
                current = lst.pop()
                res.append(current.value)
                current = current.right
            else:
                break
        return res

    @staticmethod
    def level_order_print(start):
        if start is None:
            return

        queue = Queue()
        queue.enqueue(start)
        traversal = ''
        while len(queue.items) > 0:
            traversal += str(queue.peek()) + '-->'
            pop = queue.dequeue()

            if pop.left:
                queue.enqueue(pop.left)
            if pop.right:
                queue.enqueue(pop.right)

        return traversal

    @staticmethod
    def max_level_nodes(root):
        queue = Queue()
        # from queue import Queue
        queue.enqueue(root)
        level = 0
        level_no = 0
        max_ = -1

        while len(queue.items) > 0:
            node_count = queue.size()

            if node_count > max_:
                max_ = node_count
                level_no = level

            while node_count > 0:
                pop = queue.dequeue()
                if pop.left:
                    queue.enqueue(pop.left)
                if pop.right:
                    queue.enqueue(pop.right)
                node_count -= 1
            level += 1
        print("level_no", level_no)

    @staticmethod
    def reverse_level_order_print(start):
        if start is None:
            return

        queue = Queue()
        queue.enqueue(start)
        traversal = ''
        lst = []
        while len(queue.items) > 0:
            pop = queue.dequeue()
            lst.append(pop.value)

            if pop.right:
                queue.enqueue(pop.right)
            if pop.left:
                queue.enqueue(pop.left)

        for i in range(len(lst)):
            pop = lst.pop()
            traversal += str(pop) + '-->'
        return traversal

    def height_of_tree(self, start):
        if start is None:
            return -1

        left_height = self.height_of_tree(start.left)
        right_height = self.height_of_tree(start.right)

        return 1 + max(left_height, right_height)

    def size_of_tree_reversal(self, start):
        if start is None:
            return 0
        return 1 + self.size_of_tree_reversal(start.left) + self.size_of_tree_reversal(start.right)

    @staticmethod
    def size_of_tree(start):
        if start is None:
            return

        queue = Queue()
        queue.enqueue(start)
        size = 1
        while len(queue.items) > 0:
            pop = queue.dequeue()

            if pop.left:
                queue.enqueue(pop.left)
                size += 1
            if pop.right:
                size += 1
                queue.enqueue(pop.right)

        return size

    def are_identical_tree(self, root1, root2):
        if root1 is None and root2 is None:
            return True

        if root2 is None or root1 is None:
            return False

        return root1.value == root2.value and self.are_identical_tree(root1.left, root2.left) and \
                                              self.are_identical_tree(root1.right, root2.right)

    def check_matched_subtree(self, root1, root2):
        if root1.value is None:
            return False

        if root2.value is None:
            return True

        if self.are_identical_tree(root1, root2):
            return True

        return self.check_matched_subtree(root1.left, root2) or self.check_matched_subtree(root1.right, root2)

    def skewed_tree(self, root):
        if root is None or (root.left is None and root.right is None):
            return True

        if root.left is not None and root.right is not None:
            return False

        if root.left:
            return self.skewed_tree(root.left)
        if root.right:
            return self.skewed_tree(root.right)

    def check_for_complete_binary_tree(self, root):
        no_of_nodes = self.size_of_tree_reversal(root)
        index = 0

        if self.chk_binary(root, index, no_of_nodes):
            return True
        else:
            return False

    def chk_binary(self, root, index, no_of_nodes):
        if root is None:
            return True

        if index < no_of_nodes:
            return False

        return self.chk_binary(root.left, 2*index+1, no_of_nodes) and self.chk_binary(root.right, 2*index+2, no_of_nodes)

    def sum_path_of_tree(self, root, path, sum_):
        if root is None:
            return False

        path.append(root.value)

        self.sum_path_of_tree(root.left, path, sum_)

        self.sum_path_of_tree(root.right, path, sum_)

        f = 0
        for j in range(len(path) - 1, -1, -1):
            f += path[j]
            if f == sum_:
                self.path_vector(path, j)
        path.pop(-1)

    @staticmethod
    def path_vector(path, j):
        for i in range(j, len(path)):
            print(path[j])

    def expression_tree(self, root):
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return int(root.value)

        left_sum = self.expression_tree(root.left)
        right_sum = self.expression_tree(root.right)

        if root.value == '+':
            return left_sum + right_sum
        if root.value == '*':
            return left_sum + right_sum
        if root.value == '-':
            return left_sum + right_sum
        if root.value == '/':
            return left_sum + right_sum

    def mirror_tree(self, root):
        self.in_order_print(root, '')
        self.get_mirror_tree(root)
        self.in_order_print(root, '')

    def get_mirror_tree(self, root):
        if root is None:
            return
        else:
            temp = root

            self.get_mirror_tree(root.left)
            self.get_mirror_tree(root.right)

            temp = root.left
            root.left = root.right
            root.right = temp


class BinaryOperations:
    def __init__(self):
        self.root = None

    def binary_insertion(self, start):
        if self.root is None:
            self.root = Node(start)
        else:
            self._insert(start, self.root)

    def _insert(self, start, cur_node):
        if start < cur_node.value:
            if cur_node.left is None:
                cur_node.left = Node(start)
            else:
                self._insert(start, cur_node.left)
        else:
            if cur_node.right is None:
                cur_node.right = Node(start)
            else:
                self._insert(start, cur_node.right)

    def binary_search(self, data):
        if self.root:
            is_found = self._search(data, self.root)
            if is_found:
                return True
            else:
                return False
        else:
            return None

    def _search(self, data, cur_node):
        if data < cur_node.value and cur_node.left:
            return self._search(data, cur_node.left)
        elif data > cur_node.value and cur_node.right:
            return self._search(data, cur_node.right)
        if data == cur_node.value:
            return True

    def binary_chk_property(self):
        if self.root:
            is_property = self._chk_property(self.root, self.root.value)
            if is_property is None:
                return "This is a binary tree"
            else:
                return "This is not a binary tree"

    def _chk_property(self, cur_node, data):
        if cur_node.left:
            if data > cur_node.left.value:
                return self._chk_property(cur_node.left, cur_node.left.value)
            else:
                return False
        if cur_node.right:
            if data < cur_node.value:
                return self._chk_property(cur_node.right, cur_node.right.value)
            else:
                return False

    def minimum_element(self, root):
        if root.left:
            self.minimum_element(root.left)
        else:
            print(root.value)

    @staticmethod
    def right_view_binary(root):
        q = Queue()
        lst = []
        q.enqueue(root)

        while len(q.items) > 0:
            pop = q.dequeue()
            lst.append(pop.value)

            if pop.right:
                q.enqueue(pop.right)
        print(lst)

    def left_most_node(self, root, lst):
        if root is None:
            return 0

        lst.append(root.value)
        if root.left:
            if root.left.value < root.value:
                self.left_most_node(root.left, lst)
        return lst

    def right_most_node(self, root, lst):
        if root is None:
            return 0

        lst.append(root.value)
        if root.right:
            if root.right.value > root.value:
                self.right_most_node(root.right, lst)
        return lst


if __name__ == '__main__':
    # n = Node(1)

    bt = BinaryTree(1)
    bt.root.left = Node(2)
    bt.root.right = Node(3)
    bt.root.left.left = Node(4)
    bt.root.left.right = Node(5)
    bt.root.right.left = Node(6)
    bt.root.right.right = Node(7)

    bt2 = BinaryTree(1)
    bt2.root.left = Node(2)
    bt2.root.right = Node(3)
    bt2.root.left.left = Node(4)
    bt2.root.left.right = Node(5)
    bt2.root.right.left = Node(6)
    bt2.root.right.right = Node(7)

    bt3 = BinaryTree('+')
    bt3.root.left = Node('*')
    bt3.root.right = Node('-')
    bt3.root.left.left = Node('5')
    bt3.root.left.right = Node('4')
    bt3.root.right.left = Node('100')
    bt3.root.right.right = Node('/')
    bt3.root.right.right.left = Node('20')
    bt3.root.right.right.right = Node('2')

    '''print bt.skewed_tree(bt.root)
    print bt.check_matched_subtree(bt.root, bt2.root)
    print bt.traversal_type('in-order-iterative')
    print bt.traversal_type('bst-row-count-iterative')
    print bt.traversal_type('pre-order')
    print bt.traversal_type('in-order')
    print bt.traversal_type('post-order')
    print bt.traversal_type('level-order')
    print bt.traversal_type('reverse-level-order')
    print bt.height_of_tree(bt.root)
    print bt.size_of_tree(bt.root)      # using level-order
    print bt.size_of_tree_reversal(bt.root)
    print bt.check_for_complete_binary_tree(bt.root)
    print bt.sum_path_of_tree(bt.root, [], 6)
    print bt.traversal_type('level-maximum-nodes')
    print bt3.expression_tree(bt3.root)
    bt.mirror_tree(bt.root)'''

    """ ------------------------Binary search and insertion------------------------- """

    bt = BinaryOperations()
    bt.binary_insertion(4)
    bt.binary_insertion(2)
    bt.binary_insertion(1)
    bt.binary_insertion(3)
    bt.binary_insertion(6)
    bt.binary_insertion(5)
    bt.binary_insertion(11)
    '''print bt.minimum_element(bt.root)
    print bt.binary_search(4)
    print bt.binary_chk_property()
    print bt.right_view_binary(bt.root)
    print bt.left_most_node(bt.root, [])
    print bt.right_most_node(bt.root, [])'''