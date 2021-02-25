class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        return self.head

    def append_at_end(self, data):
        new_node = Node(data)
        new_node.next = None
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node

    def length(self):
        cur = self.head
        total = 0
        while cur is not None:
            total += 1
            cur = cur.next
        return total

    def display(self):
        elem = []
        cur_node = self.head
        while cur_node:
            elem.append(cur_node.data)
            cur_node = cur_node.next
        print elem

    def get(self, index):
        if index >= self.length():
            print "ERROR"
            return None
        cur_idx = 0
        cur_node = self.head
        while True:
            if cur_idx == index:
                return cur_node.data
            cur_node = cur_node.next
            cur_idx += 1

    def erase(self, index):
        if index >= self.length():
            print "ERROR"
            return None
        cur_idx = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            if cur_idx == index:
                last_node.next = cur_node.next
                return
            cur_node = cur_node.next
            cur_idx += 1

    def reverse(self):
        prev = None
        cur = self.head

        while cur is not None:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        self.head = prev

    '''
    def reverse_k_elems(self, val):
        count = 1
        temp = self.head
        while count < 3:
            temp = temp.next
            count += 1

        print temp
        joint_point = temp.next
        temp.next = None

        prev = None
        cur = self.head
        while cur is not None:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        self.head = prev
        cur = self.head

        while cur.next is not None:
            cur = cur.next
        cur.next = joint_point
        return self.head
        '''

    def reverse_k_elements(self, val):
        prev = None
        cur = self.head
        count = 0

        while cur is not None and count < 3:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

            count += 1

        self.head = prev
        cur_other_hlf = cur
        cur1 = self.head

        while cur1.next is not None:
            cur1 = cur1.next

        cur1.next = cur_other_hlf
        return self.head

    def remove_duplicates(self):
        cur = self.head
        while cur is not None:
            cur2 = cur
            while cur2.next is not None:
                if cur.data == cur2.next.data:
                    dup = cur2.next
                    cur2.next = cur2.next.next
                    del dup
                else:
                    cur2 = cur2.next
            cur = cur.next

    def rotate_linked_list(self, key):
        cur = self.head
        count = 1
        if key > self.length():
            return "Not Possible"

        while cur is not None and count < key:
            cur = cur.next
            count += 1
        kthnode = cur
        while cur.next is not None:
            cur = cur.next

        cur.next = self.head
        # print kthnode.data, self.head.data
        self.head = kthnode.next
        kthnode.next = None

    def delete_middle_element(self):
        fast_ptr = self.head
        slow_ptr = self.head
        prev = None

        while fast_ptr is not None and fast_ptr.next is not None:
            fast_ptr = fast_ptr.next.next
            prev = slow_ptr
            slow_ptr = slow_ptr.next

        prev.next = slow_ptr.next
        del slow_ptr

    def reverse_alternate_nodes(self):
        current_ptr = self.head
        odd_ptr = Node()
        count = 0
        prev = None
        lst = []

        while current_ptr is not None:
            if count % 2 != 0:
                temp = current_ptr
                lst.append(temp)
                prev.next = current_ptr.next
                current_ptr = current_ptr.next
                del temp
            else:
                prev = current_ptr
                current_ptr = current_ptr.next
            count += 1

        # lst = lst[::-1]
        for i in lst:
            self.append_at_end(i.data)

    def delete_first_node(self):
        cur = self.head
        prev = None

        while cur is not None and cur.next is not None:
            cur.data = cur.next.data
            prev = cur
            cur = cur.next
        prev.next = None


if __name__ == '__main__':
    mylist = LinkedList()
    mylist.append(5)
    mylist.append(4)
    mylist.append(3)
    mylist.append(2)
    mylist.append(1)
    # mylist.display()
    # mylist.reverse()
    # mylist.display()
    # mylist.get(2)
    # mylist.erase(1)
    # print(mylist.length())
    # mylist.reverse_k_elems(3)
    # mylist.reverse_k_elements(3)

    mylist.append_at_end(4)
    mylist.append_at_end(2)
    # mylist.display()
    mylist.remove_duplicates()
    mylist.display()
    # mylist.rotate_linked_list(3)
    # mylist.display()
    # mylist.delete_middle_element()
    # mylist.display()
    # mylist.reverse_alternate_nodes()
    # mylist.delete_first_node()
    # mylist.display()


