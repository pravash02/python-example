"""

Kadane's Algorithm
-------------------

Kadane's algorithm is used to find the maximum sub-array sum for a given array.
Basically this algorithm is to look for all positive contiguous segments of the array.
And keep track of maximum sum contiguous segment among all positive segments.

These are used in finding such as 'Longest Sum Contiguous', 'Maximum Sub-Array Contiguous'

 Step1: Initialize the 2 variables with arrays first element.
        max_current = list[0]
        max_global = list[0]
 Step2: Run a loop from the arrays second position till the end of the array.

        Then check the maximum of the arrays in current position(list[1]) and the sum of the
        max_current(previous position i.e list[0]) and current position(list[1])
        Assign the maximum to the max_current.

        Also update the max_global with the max_current if it is larger than max_global
 Step3: Return the max_global
"""


def max_sub_array(lst):
    lst2 = []
    max_cur = max_global = lst[0]

    for i in range(1, len(lst)-1):
        max_cur = max(lst[i], max_cur + lst[i])

        if max_cur > max_global:
            max_global = max_cur
            lst2.append([lst[i]])
    return max_global, lst2


if __name__ == '__main__':
    print(max_sub_array([3, 2, 6, -1]))
