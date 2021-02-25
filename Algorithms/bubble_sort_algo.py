"""

Bubble Sort Algorithm
------------------------

 Step1: Bubble Sort is a simple sorting algorithm that repeatedly swaps two adjacent elements through iterations
        through the list length to create a sort list.
"""


def bubble_sort(lst):
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, len(lst) - 1):
            if lst[i] > lst[i+1]:
                sorted = False
                lst[i], lst[i+1] = lst[i+1], lst[i]
    return lst


if __name__ == '__main__':
    print(bubble_sort([2, 4, 3, 5, 7, 6]))
