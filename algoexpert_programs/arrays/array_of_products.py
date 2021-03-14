"""
Given an array arr[] of n integers, construct a Product Array prod[] (of same size)
such that prod[i] is equal to the product of all the elements of arr[] except arr[i]

Input: [10, 3, 5, 6, 2]
Output: [180, 600, 360, 300, 900]

"""
from functools import reduce


def arr_of_products(arr):

    new_lst = []
    for i in range(0, len(arr)):

        right_mul = 1
        left_mul = 1

        if len(arr[i+1:]) != 0:
            right_mul = reduce(lambda x, y: x*y, arr[i+1:])
        if len(arr[:i]) != 0:
            left_mul = reduce(lambda x, y: x * y, arr[:i])

        new_lst.append(right_mul * left_mul)

    return new_lst


if __name__ == '__main__':
    arr = [10, 3, 5, 6, 2]

    print(arr_of_products(arr))
