class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class AddTwoNumbers:
    def __init__(self):
        self.head = None

    def append_at_front(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        return self.head

    def append_at_end(self, val):
        new_node = Node(val)
        new_node.next = None
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node

    def get_linked_list(self, l):
        for i in l:
            self.append_at_front(i)

    def display(self):
        ll = []
        current = self.head

        while current:
            ll.append(current.data)
            current = current.next
        return ll

    def addTwoNumbers(self, l1, l2):
        sum1 = "".join(str(i) for i in l1)
        sum2 = "".join(str(i) for i in l2)
        res = int(sum1) + int(sum2)
        print res
        self.get_linked_list(list(str(res)))
        return self.display()


def twoSum(nums, target):
    hash_table = {}
    for i, num in enumerate(nums):
        if target - num in hash_table:
            return [hash_table[target - num], i]
            break
        hash_table[num] = i
    return


def lengthOfLongestSubstring(s):
    d = {}
    start = count = 0
    for i in range(len(s)):
        if s[i] in d and start <= d[s[i]]:
            start = d[s[i]] + 1
        else:
            count = max(count, i-start+1)
        d[s[i]] = i
    print count


def sum_of_consecutive_subarray(s, k):
    max_sum = 0
    cur_sum = 0
    for i in range(len(s)):
        cur_sum += s[i]
        if i >= k - 1:
            max_sum = max(max_sum, cur_sum)
            cur_sum -= s[i - (k - 1)]

    return max_sum


def median_of_2arrays(l1, l2):
    if len(l1) > len(l2):
        return median_of_2arrays(l2, l1)

    x = len(l1)
    y = len(l2)

    low = 0
    high = x

    while low <= high:
        partition_x = (low + high) / 2
        partition_y = ((x + y + 1) / 2) - partition_x

        max_left_x = float('-inf') if partition_x == 0 else l1[partition_x - 1]
        min_right_x = float('inf') if partition_x == x else l1[partition_x]

        max_left_y = float('-inf') if partition_y == 0 else l2[partition_y - 1]
        min_right_y = float('inf') if partition_y == y else l2[partition_y]

        if max_left_x <= min_right_y and max_left_y <= min_right_x:
            if (x + y) % 2 == 0:
                return (max(max_left_x, max_left_y) + min(min_right_y, min_right_x)) / 2
            else:
                return max(max_left_x, max_left_y)
        elif max_left_x > min_right_y:
            high = partition_x - 1
        else:
            low = partition_x + 1


def zigzag_conversion(s, period):
    r = []
    if period > len(s) or period <= 1:
        return s

    interval = (2*period) - 2
    for i in range(0, period):
        step = interval - (2*i)
        for j in range(i, len(s), interval):
            r.append(s[j])
            if (step > 0) and (step < interval) and ((j + step) < len(s)):      # this is for middle row
                r.append(s[j + step])
    return r


if __name__ == '__main__':
    lst1 = AddTwoNumbers()
    lst2 = AddTwoNumbers()
    lst3 = AddTwoNumbers()
    lst1.get_linked_list([2, 4, 3])
    l1 = lst1.display()
    lst2.get_linked_list([5, 6, 9])
    l2 = lst2.display()
    # print(lst3.addTwoNumbers(l1, l2))
    # print(twoSum([2, 4, 3, 90], 6))
    # print(lengthOfLongestSubstring('abcabcbb'))
    # print(sum_of_consecutive_subarray([1, 2, 3, 4, 5, 6, 1, 2], 3))
    # print(median_of_2arrays([1, 3, 8, 9, 15], [7, 11, 19, 21, 18, 25]))
    print(zigzag_conversion('PAYPALISHIRING', 3))




















# addTwoNumbers (2nd approach)
'''
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2

        ret_head = l1
        carry = 0

        while l1 is not None and l2 is not None:
            tmp = l1.val + l2.val + carry
            carry = tmp / 10
            l1.val = tmp % 10
            if l1.next is None or l2.next is None:
                break
            l1 = l1.next
            l2 = l2.next

        if l1.next is None:
            l1.next = l2.next

        while carry != 0:
            if l1.next is None:
                l1.next = ListNode(0)
            l1 = l1.next
            tmp = l1.val + carry
            l1.val = tmp % 10
            carry = tmp / 10

        return ret_head


def list2link(l):
    if len(l) == 0:
        return None
    ret_tail = ret_head = ListNode(l[0])
    for val in l[1:]:
        tmp = ListNode(val)
        ret_tail.next = tmp
        ret_tail = ret_tail.next
    return ret_head


def print_link(link):
    while link is not None:
        print "->%d" % link.val,
        link = link.next
    print "\n"


if __name__ == '__main__':
    solution = Solution()
    print_link(solution.addTwoNumbers(list2link([2, 7, 8, 9, 9, 9]), list2link([3, 7, 5])))
    print_link(solution.addTwoNumbers(list2link([2, 4, 3]), list2link([5, 6, 4])))
'''
