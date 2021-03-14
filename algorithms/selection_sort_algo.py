"""

Selection Sort Algorithm
------------------------

 Step1: The Selection Sort Algorithm starts by setting the first item in an unsorted list as the position with the
        lowest (minimum) value. We then use this to compare each of the items to the right.
        Whenever we find a new item with a lower value, that becomes our new minimum value and we continue on.

 Step2: After one iteration of the selection sort algorithm, we create two sublists.
        One will be for unsorted items and the other will be for sorted ones. We move the minimum item from
        the unsorted sublist into the last position of our sorted sublist.

 Step3: After we finish all the iterations, we should be left with only the largest number in our
        unsorted sublist (which is now sorted to the highest position as it is the highest value).
"""


def selection_sort(lst):
    length = len(lst)
    for i in range(0, length):
        min_val = i

        for j in range(i+1, length):
            if lst[j] < lst[min_val]:
                min_val = j
        if min_val != i:
            lst[i], lst[min_val] = lst[min_val], lst[i]
    return lst


if __name__ == '__main__':
    print(selection_sort([2, 4, 3, 5, 7, 6]))
