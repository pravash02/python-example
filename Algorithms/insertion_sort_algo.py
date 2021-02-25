"""

Insertion Sort Algorithm
------------------------

 Step1: The insertion sort algorithm breaks a list into two sublists, one with sorted values and the other
        with unsorted values. We move one unsorted value to the sorted sublist, and compare its value to the
        values to the left. We move it into the correct position by switching, each time the item to the left is larger.

 Step2: One we have sorted the element, we start the next iteration and sort the next unsorted item in the
        unsorted sublist..
"""


def insertion_sort(lst):
    length = len(lst)
    i = 1
    for i in range(1, length):
        while lst[i] < lst[i - 1] and i > 0:
            lst[i], lst[i - 1] = lst[i - 1], lst[i]
            i -= 1
    return lst


if __name__ == '__main__':
    print(insertion_sort([2, 4, 3, 5, 7, 6]))
