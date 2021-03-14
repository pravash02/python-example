"""

Boyer-Moore Algorithm
---------------------

The boyer moore string search is an ingenious piece of search algorithm.

These are used in finding such as 'Matching Pattern', 'Search a Substring/Pattern'

 Step1: Make a "Bad Match Table" of characters.
        Formula used - "max(1, Length_Of_Pattern - Each characters Actual Index - 1)"
        ex - TEST
                     -----------------------
                    |    T   |    E   |   S |
                     --------|--------|-----
                    |    1   |   2    |  1  |
                     -----------------------

        Using the above formula we Iterate through the pattern and compute the values to the bad match table.
        And keep updating the old values for the same character.

 Step2: We begin the comparisons form the last character in the pattern move backwards
 Step3: If pattern character mismatches with text character and if the character doesn't appear anywhere in 
        the pattern, complete past that character otherwise shift the pattern to align with that character 
        with last occurrences of the character.
"""

from collections import OrderedDict
from collections import Counter


def pattern_search(char, pattern):
    char_size = len(char)
    pattern_size = len(pattern)
    max_shift_dict = OrderedDict()

    for i in range(0, pattern_size):
        max_shift = max(1, pattern_size - i - 1)
        max_shift_dict[pattern[i]] = max_shift

    i = 0
    occurrences = []
    while i <= (char_size - pattern_size):
        num_of_skips = 0
        flag = False
        for j in range(pattern_size - 1, -1, -1):
            if pattern[j] != char[i + j]:
                if char[i + j] in max_shift_dict.keys():
                    num_of_skips = max_shift_dict[char[i + j]]
                    flag = True
                    break
                else:
                    num_of_skips = pattern_size
                    flag = True
                    break
            if not flag:
                num_of_skips = pattern_size
                occurrences.append(i)
        i += num_of_skips

    counter_lst = Counter(occurrences)
    for keys in counter_lst:
        if counter_lst[keys] == pattern_size:
            print keys


if __name__ == '__main__':
    print(pattern_search("THIS IS A TEST", "ST"))
