"""
To find all the pairs of two integers in an unsorted array that sum up to a given Sum

Example -
    array = [3, 5, 2, -4, 8, 11], sum = 7

    result = [[11, -4], [2, 5]]

"""

def twoSum(arr, s):
    iter_id = 0
    res_list = []
    arr_len = len(arr)

    for i in range(iter_id, arr_len):
        arr_id = iter_id

        while arr[arr_id] != arr[-1]:
            if (arr[i] + arr[arr_id+1]) == s:
                res_list.append([arr[i], arr[arr_id+1]])
            else:
                pass

            arr_id += 1

        iter_id += 1
        arr_len -= 1
    return res_list


def twoSum_2(arr, s):
    iter_id = 0
    res_list = []

    for i in arr:

        other_num = s - i
        if other_num in arr[iter_id:]:
            res_list.append([i, other_num])

        iter_id += 1
    return res_list


if __name__ == '__main__':
    array = [3, 5, 2, -4, 8, 11]
    _sum = 7

    print(twoSum(array, _sum))
    print(twoSum_2(array, _sum))

