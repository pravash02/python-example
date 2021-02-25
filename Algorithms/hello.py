from collections import deque, Counter
import heapq

print("hello world")


def sum13():
    """
    Return the sum of the numbers in the array, returning 0 for an empty array.
    Except the number 13 is very unlucky,
    so it does not count and numbers that come immediately after a 13 also do not count

    :return:
    """
    n = [1, 2, 3, 13, 13]
    if len(n) == 0:
        print(0)
    i = 0
    sum1 = 0
    while i < len(n):
        if n[i] != 13:
            sum1 += n[i]
        else:
            i += 1
        i += 1

    print(sum1)
    return sum1


def rotate_left3():
    """
    Given an array of ints length 3,
    return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}

    :return:
    """
    int_list = [1, 2, 3]
    lst = []

    i = 0
    while i < len(int_list):
        if i == len(int_list) - 1:
            lst.append(int_list[0])
        else:
            lst.append(int_list[i + 1])
        i += 1

    print(lst)
    return lst


def sum67():
    """
    Return the sum of the numbers in the array,
    except ignore sections of numbers starting with a 6 and extending to the next 7
    (every 6 will be followed by at least one 7).
    Return 0 for no numbers.

    :return:
    """
    flag = False
    int_sum = 0
    int_list = [1, 2, 3, 6, 33, 33, 7, 1, 2, 6, 4, 4, 7]

    for num in int_list:
        if num == 6:
            flag = True
            continue
        if num == 7 and flag is True:
            flag = False
            continue
        if flag is False:
            int_sum += num

    print(int_sum)
    return int_sum


def has22():
    """
    Given an array of ints,
    return True if the array contains a 2 next to a 2 somewhere.

    :return:
    """
    int_list = [1, 2, 2, 3]

    flag = False
    for i in range(0, len(int_list) - 1):
        if int_list[i:i + 2] == [2, 2]:
            flag = True

    print(flag)
    return flag


def get_duplicate_integers():
    """
    Get the duplicate integers from the given list

    :return:
    """
    int_list = [1, 2, 2, 3, 4, 5, 6, 6, 9, 10]
    int_dict = {}
    count = 0

    for i in int_list:
        if i in int_dict.keys():
            int_dict[i] = int_dict[i] + 1
        else:
            int_dict[i] = count + 1

    print(int_dict)
    return int_dict


def cigar_party(cigars, is_weekend):
    if is_weekend:
        if cigars >= 40:
            return True
        else:
            return False
    elif 40 <= cigars <= 60:
        return True
    else:
        return False


def date_fashion(you, date):
    if you <= 2 or date <= 2:
        return 0
    elif you >= 8 or date >= 8:
        return 2
    else:
        return 1


def caught_speeding(speed, is_birthday):
    small_ticket = 61
    big_ticket = 81
    if is_birthday:
        small_ticket = small_ticket + 5
        big_ticket = big_ticket + 5
    if speed <= small_ticket:
        return 0
    elif small_ticket <= speed <= big_ticket:
        return 1
    elif speed >= big_ticket:
        return 2


def squirrel_play(temp, is_summer):
    if is_summer:
        if 60 <= temp <= 100:
            return True
        else:
            return False
    else:
        if 60 <= temp <= 90:
            return True
        else:
            return False


def alarm_clock(day, vacation):
    weekdays = [1, 2, 3, 4, 5]
    if vacation:
        if day in weekdays:
            return "10:00"
        else:
            return "off"
    else:
        if day in weekdays:
            return "7:00"
        else:
            return "10:00"


def most_frequent(list1):
    counter = 0
    num = 0

    for i in list1:
        curr_frequency = list1.count(i)
        if curr_frequency > counter:
            counter = curr_frequency
            num = i

    print(num)
    return num


def common_elements(a, b):
    a.sort()
    b.sort()
    i, j = 0, 0
    common = []
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            common.append(a[i])
            i += 1
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            j += 1

    print(common)
    return common


def rotate_list(lst1, lst2):
    d = deque(lst1)
    d.rotate(-2)

    if list(d) == lst2:
        print(True)
    else:
        print(False)


def get_next_element_in_list(lst):
    print(lst)
    lst = lst[::-1]
    carry = 1
    count = 0
    new_lst = []
    for i in range(len(lst)):
        if lst[i] == 9 and carry == 1:
            new_lst.append((lst[i] + carry) % 10)
            count += 1
            carry = 1
            if count == len(lst):
                new_lst.append(carry)
        else:
            new_lst.append(lst[i] + carry)
            carry = 0

    print(new_lst[::-1])
    return new_lst[::-1]


def get_staircase_steps(stairs_no):
    dict1 = {}
    total = 0
    if stairs_no == 0 or stairs_no == 1:
        total += 1
        dict1.update({stairs_no: total})
    else:
        dict1 = {}
        for j in [1, 3, 5]:
            if stairs_no - j >= 0:
                total = 0
                total += get_recur_recs(stairs_no)
                dict1.update({j: total})
    print(dict1)
    print(total)
def get_recur_recs(n):
    if n <= 1:
        return 1
    else:
        return get_recur_recs(n-1) + get_recur_recs(n-2)


def get_gas_station(gas, cost):
    total = 0
    start = 0
    remaining_sum = 0
    for i in range(len(gas)):
        remaining = gas[i] - cost[i]
        print(remaining)
        if remaining_sum >= 0:
            remaining_sum += remaining
        else:
            remaining_sum = remaining
            start = i
        total += remaining

    if total >= 0:
        print(start)
        return start
    else:
        return -1


def get_majority_element(n):
    element_count = Counter(n)
    for k, v in element_count.items():
        if v > len(n)/2:
            print(k)


def get_distinct_subsequences(a, b):
    if a == b:
        print(1)
    else:
        print(Counter(a))
        print(Counter(b))
        for i in range(0, 2):
            pass


def get_character(char):
    print(char)
    valid_chars = ['314', '49', '15926535897', '14', '9323', '8462643383279', '4', '793']
    char_lst = list(char)
    substr = ''
    lst = []
    prev_index = None

    for i in range(len(char_lst) + 1):
        if substr in valid_chars:
            lst.append(substr)
            lst.append(' ')
            substr = ''
            prev_index = i
        else:
            if prev_index is not None:
                substr = substr + char_lst[prev_index] + char_lst[i]
                prev_index = None
            else:
                substr = substr + char_lst[i]
    print("".join(lst))


def get_arrows(lst):
    max_ = max(lst)
    count = 0

    # while len(lst) != 0:
    while len(lst) != 0:
        j = 0
        for i in range(len(lst)):
            if max_ == lst[j]:
                lst.pop(j)
                max_ -= 1
            else:
                j += 1
        if len(lst) != 0:
            max_ = max(lst)
        count += 1
    print("no of arrows required - ", count)


if __name__ == '__main__':
    sum13()
    rotate_left3()
    nums = [1, 2, 3, 6, 33, 33, 7, 1, 2, 6, 4, 4, 7]
    sum67()
    has22()
    get_duplicate_integers()
    # list1 = [2, 1, 2, 2, 1, 3]
    # most_frequent(list1)
    # map(str, common_elements([1, 2, 4, 8], [1, 4, 9]))
    # rotate_list([1, 2, 3, 4, 5], [3, 4, 5, 1, 2])
    # get_next_element_in_list([2, 9, 9, 7])
    # get_staircase_steps(4)
    # get_gas_station([2, 1], [1, 2])
    # get_majority_element([2, 3, 2])
    # get_distinct_subsequences("abbc", "abc")
    # get_character("3141592653589793238462643383279")
    # get_arrows([5, 4, 4, 3, 3])
