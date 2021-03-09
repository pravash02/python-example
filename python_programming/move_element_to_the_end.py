"""
  You're given an array of integers and an integer. Write a function that moves
  all instances of that integer in the array to the end of the array and returns
  the array.
  The function should perform this in place (i.e., it should mutate the input
  array) and doesn't need to maintain the order of the other integers.

"""


def moveElement(arr, toMove):

    _index = 0

    for i in range(0, len(arr)-1):
        print(_index, arr)
        if arr[_index] == toMove:
            arr.append(arr.pop(_index))
            _index -= 1

        _index += 1

    return arr


if __name__ == '__main__':
    arr = [1, 2, 3, 2, 2, 5]
    toMove = 2

    print(moveElement(arr, toMove))
