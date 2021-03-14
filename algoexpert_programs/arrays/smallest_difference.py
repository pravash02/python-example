"""
compute the pair of values (one value in each array)
with the smallest (non-negative) difference.

Input : A[] = {l, 3, 15, 11, 2}
        B[] = {23, 127, 235, 19, 8}
Output : 3

"""


def smmallest_diff(a, b):
    a.sort()
    b.sort()
    _dict = {}
    k = 0
    l = 0

    SMALL_DIFF = float('inf')

    for i in range(k, len(a)):
        print(a[i], k)
        for j in range(l, len(b)):
            print(b[j], l)
            if abs(a[i] - b[j]) < SMALL_DIFF:
                _dict[abs(a[i] - b[j])] = [a[i], b[j]]
                SMALL_DIFF = abs(a[i] - b[j])
                k += 1
                break
            elif abs(a[i] - b[j]) > SMALL_DIFF:
                l += 1
                break
            else:
                k += 1
                l += 1
                break

    return min(_dict.items(), key=lambda x: x[0])


if __name__ == '__main__':
    arr1 = [1, 3, 15, 11, 2]
    arr2 = [23, 127, 235, 19, 8]

    print('smallest pair', smmallest_diff(arr1, arr2))
