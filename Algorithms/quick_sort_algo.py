"""

Quick Sort Algorithm
---------------------

Sorting algorithm uses the idea of DIVIDE and CONQUER

 Step1: Bring the pivot to its appropriate position such that left of the pivot is smaller
        and right is greater
 Step2: Quick sort the left part
 Step3: Quick sort the right part

"""


def quick_sort_iterative():
    pass


def quick_sort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()

    item_grt = []
    item_low = []

    for item in sequence:
        if item < pivot:
            item_low.append(item)
        else:
            item_grt.append(item)

    return quick_sort(item_low) + [pivot] + quick_sort(item_grt)


def quick_sort_recursive(a, low, high):
    if low < high:
        p = get_partition(a, low, high)
        quick_sort_recursive(a, low, p-1)
        quick_sort_recursive(a, p+1, high)
    return a


def get_partition(a, low, high):
    pivot = a[high]
    i = low - 1

    for j in range(low, high):
        if a[j] < pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[high] = a[high], a[i+1]
    return i+1


if __name__ == '__main__':
    # quick_sort_iterative()
    print(quick_sort([7, 5, 1, 3, 4]))
    lst = [2, 3, 1, 6, 5, 4]
    print(quick_sort_recursive(lst, 0, len(lst) - 1))
