"""
To find all the pairs of three integers in an unsorted array that sum up to a given Sum

Example -
    Input array: [7, 12, 3, 1, 2, -6, 5, -8, 6]
    Target sum: 0

    Output: [[2, -8, 6], [3, 5, -8], [1, -6, 5]]

"""


def threeSum(arr, s):
    _lst = []
    arr.sort()
    for i in range(0, len(arr) - 1):
        _len = len(arr) - 1
        k = i + 1
        # while k < _len:
        for j in range(k + 1, _len):
            if (arr[i] + arr[k] + arr[_len]) == s:
                print('matched', [arr[i], arr[k], arr[_len]])
                temp = sorted([arr[i], arr[k], arr[_len]])
                if temp not in _lst:
                    _lst.append(temp)
                k += 1
                _len -= 1
            elif (arr[i] + arr[k] + arr[_len]) < s:
                k += 1
            else:
                _len -= 1

    return _lst


if __name__ == '__main__':
    array = [7, 12, 3, 1, 2, -6, 5, -8, 6]
    _sum = 0

    print(threeSum(array, _sum))
