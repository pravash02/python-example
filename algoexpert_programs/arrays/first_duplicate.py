"""
To find the first duplicate in a list of values.

    Input: [1,2,3,3,2,1]
    Output: 3 is the first duplicate

"""


def first_duplicate(arr):
    new_lst = set()

    for i in arr:
        if i in new_lst:
            return "{} is the duplicate".format(i)
        else:
            new_lst.add(i)
    return "No duplicates found"


if __name__ == '__main__':
    arr = [1, 2, 3, 3, 2, 1]
    print(first_duplicate(arr))
