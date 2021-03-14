"""
Given an array of integers. Find a peak element in it.
An array element is a peak if it is NOT smaller than its neighbours.

    Input: [20, 10, 15, 2, 23, 90, 67]
    Output: [20, 15, 90]

"""


def peak_element(arr):
    new_lst = []

    if len(arr) == 1:
        return [arr[0]]

    if arr[len(arr) - 1] > arr[len(arr) - 2]:
        new_lst.append(arr[len(arr) - 1])

    if arr[0] > arr[1]:
        new_lst.append(arr[0])

    for i in range(1, len(arr)-1):
        if arr[i + 1] < arr[i] > arr[i - 1]:
            new_lst.append(arr[i])

    return new_lst


if __name__ == '__main__':
    arr = [20, 10, 15, 2, 23, 90, 67]
    print(peak_element(arr))
