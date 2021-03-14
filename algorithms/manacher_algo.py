"""

Manacher's Algorithm
---------------------

Basically used in finding palindromic substring a given string

 according to the below example
 Step1: Loop through the string, have one indicator 'i' for finding the next palindrome and 'c' is setting the
        current palindrome, 'r' is right boundary, 'p' for storing the count of possible palindromes.
 Step2: Need to remember 2 rules -
        if right boundary is less than the palindrome, then move the c to the ith position(net palindrome center)
        and right boundary with the position of the last character of the palindrome
        if right boundary is more than the palindrome, update the list 'p' = min(r - i, p[mirror])
"""


def preprocess_string(string):
    new_string = string
    lst = []

    for i in range(0, len(new_string)):
        lst.append(new_string[i])
        lst.append('#')
    string = "".join(lst)
    string = '@#' + string + '$'  # Adding @,$ to set the limits/boundaries
    return string


def longest_palindrome(string):
    string = preprocess_string(string)

    c = r = 0
    p = [0]*len(string)
    i = 1

    for i in range(1, len(string) - 1):
        mirror = 2*c - i

        if i < r:
            p[i] = min(r - i, p[mirror])

        while string[i + (1 + p[i])] == string[i - (1 + p[i])]:
            p[i] += 1

        if i + p[i] > r:
            c = i
            r = i + p[i]
    print c


if __name__ == '__main__':
    print(longest_palindrome("ABABABA"))
