def lengthOfLongestSubstring(s):
    d = {}
    start = count = 0
    for i in range(len(s)):
        if s[i] in d and start <= d[s[i]]:
            start = d[s[i]] + 1
        else:
            count = max(count, i-start+1)
        d[s[i]] = i
    print count


def sumOfConsecutiveSubArray(s, k):
    max_sum = 0
    cur_sum = 0
    for i in range(len(s)):
        cur_sum += s[i]
        if i >= k - 1:
            max_sum = max(max_sum, cur_sum)
            cur_sum -= s[i - (k - 1)]

    return max_sum


if __name__ == '__main__':
    print(lengthOfLongestSubstring('abcabcbb'))
    print(sumOfConsecutiveSubArray([1, 2, 3, 4, 5, 6, 1, 2], 3))
