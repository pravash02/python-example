"""
Check if a list is subsequence of another list in order

Example -
    array = [1, 2, 3, 4]
    sequence1 = [1, 3, 4], sequence2 = [2, 4]

    result = 'True' for both the sequence

"""

def isValidSubsequence(arr, seq):
    count = 0
    seq_len = len(seq)

    for i in arr:
        while len(seq) > 0:
            if i == seq[0]:
                count += 1
                del seq[0]
            break

    if count == seq_len:
        return True
    else:
        return False


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5]
    sequence = [1, 4]

    print(isValidSubsequence(array, sequence))
