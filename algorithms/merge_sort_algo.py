"""

Merge Sort Algorithm
---------------------

Sorting algorithm uses the idea of DIVIDE and CONQUER

 Step1:
 Step2:
 Step3:

"""


def merge_sort_recursive(a):
    if len(a) <= 1:
        return a

    left = merge_sort_recursive(a[:len(a)/2])
    right = merge_sort_recursive(a[len(a)/2:])
    return merge(left, right)


def merge(l, r):
    i = j = 0
    c = []

    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            c.append(l[i])
            i += 1
        else:
            c.append(r[j])
            j += 1
    if i == len(l):
        c.extend(r[j:])
    else:
        c.extend(l[i:])
    return c


if __name__ == '__main__':
    lst = [2, 3, 1, 6, 5, 4]
    print(merge_sort_recursive(lst))
