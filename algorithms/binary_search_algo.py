"""

Binary Search Algorithm
-----------------------

Binary Search Takes a sorted sequence of elements and figures out if a given element
is within that sequence

 Step1: We'll do this with a series of repeated comparisons.
 Step2: We compare the middle number of our sequence to the item we're searching for.
        This determines if we continue looking right or left of the midpoint.

"""


def binary_search(item, lst):
    start = 0
    end = len(lst) - 1

    for i in range(start, end):
        mid_point = start + (end-start) // 2
        mid_item = lst[mid_point]

        if item == mid_item:
            return 'position ', mid_point
        elif item < mid_item:
            end = mid_point - 1
        else:
            start = mid_point + 1
    return None


if __name__ == '__main__':
    lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(binary_search(4, lst1))
