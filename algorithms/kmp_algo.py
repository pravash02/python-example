"""

Knuth-Morris-Pratt (KMP)
------------------------

The basic idea behind KMP's algorithm is: whenever we detect a mismatch (after some matches), we already know some of
the characters in the text of the next window.We take advantage of this information to avoid matching the characters
that we know will anyway match. Let us consider below example to understand this.

 Step1: Find length of 2 arrays: Actual text and pattern, and also create a lps array which is
        of same size as that of pattern.
            txt_size = len(txt)
            pattern_size = len(pattern)
            lps = [0]*pattern_size
 Step2: LPS Computation.
        check for the longest suffix which is also the prefix
"""


def lps_computation(pattern, pattern_size, lps_lst):
    i = 0
    j = 1
    lps_lst[0] = 0

    while j < pattern_size:
        if pattern[j] == pattern[i]:
            lps_lst[j] = i + 1
            i += 1
            j += 1
        else:
            if i != 0:
                i = lps_lst[i - 1]
            else:
                lps_lst[j] = 0
                j += 1
    return lps_lst


def substring_search(txt, pattern):
    txt_size = len(txt)
    pattern_size = len(pattern)
    lps_lst = [0]*pattern_size

    lps_lst = lps_computation(pattern, pattern_size, lps_lst)

    i = 0
    j = 0
    while i < txt_size:
        if txt[i] == pattern[j]:
            i += 1
            j += 1
        else:
            if j != 0:
                j = lps_lst[j - 1]
            else:
                i += 1
        if j == pattern_size:
            print(i-j)
            j = lps_lst[j - 1]


if __name__ == '__main__':
    print(substring_search("THIS IS A TEST", "IS"))
