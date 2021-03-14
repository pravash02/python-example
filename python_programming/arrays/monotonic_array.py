"""
An array is monotonic if it is either monotone increasing or
monotone decreasing.
    Input: [1,2,2,3]
    Output: true

    Input: [6,5,4,4]
    Output: true

    Input: [1,1,1]
    Output: true

"""


def monotonic_array_simple_method(a, c, b):

    flag_small = None
    flag_grt = None

    count = 1

    for i in range(0, len(a) - 1):
        if a[i] <= a[i+1]:
            if not flag_grt:
                flag_small = True
                count += 1
            else:
                count -= 1

        elif a[i] >= a[i+1]:
            if not flag_small:
                flag_grt = True
                count += 1
            elif flag_small & len(set(a[:i])):
                count += 1
            else:
                count -= 1

        else:
            if flag_small or flag_grt:
                count -= 1

    if flag_small or flag_grt:
        if count == len(a):
            return True
        else:
            return False


def monotonic_array(a, b, c):

    return (all(a[i] <= a[i + 1] for i in range(len(a)-1)) or
            all(a[i] >= a[i + 1] for i in range(len(a)-1)))


if __name__ == '__main__':
    arr1 = [1, 2, 2, 3, 0, 4]
    arr2 = [6, 5, 4, 4, 7, 2]
    arr3 = [1, 1, 1]

    # print(monotonic_array(arr1, arr2, arr3))
    print(monotonic_array_simple_method(arr1, arr2, arr3))
