import sys


class DynamicProgramming:
    def __init__(self):
        self.value = {0: 0, 1: 1}
        self.sum = []
        self.sub_arr = []

    def bytelandian_gold(self, inp):
        if inp in self.value:
            return inp
        else:
            self.value[inp] = max(inp, self.bytelandian_gold(inp // 2) + self.bytelandian_gold(
                inp // 3) + self.bytelandian_gold(inp // 4))
        return self.value[inp]

    def min_cost_path(self, lst1, m, n):
        if m < 0 or n < 0:
            return sys.maxsize
        elif m == 0 and n == 0:
            return lst1[m][n]
        else:
            return lst1[m][n] + min(self.min_cost_path(lst1, m - 1, n - 1),
                                    self.min_cost_path(lst1, m - 1, n),
                                    self.min_cost_path(lst1, m, n - 1))

    def sum_subset(self, lst2, sum2):
        if len(lst) == 0:
            return 0
        else:
            for i in range(0, len(lst2)):
                for j in range(i + 1, len(lst2)):
                    val = int(lst2[i]) + int(lst2[j])
                    if val == sum2:
                        self.sum.append(lst2[i])
                        self.sum.append(lst2[j])
        return self.sum

    def printCountRec(self, dist):
        if dist < 0:
            return 0
        if dist == 0:
            return 1

        return (self.printCountRec(dist - 1) +
                self.printCountRec(dist - 2) +
                self.printCountRec(dist - 3))

    def towerhopper(self, towers):
        size = len(towers)
        count = 0
        current = 0
        while True:
            if current >= size:
                return count, True
            if current <= size:
                count += 1
                print current, True
            if size == 0:
                return False
            current = self.get_net_pos(current, towers)

    def get_net_pos(self, current, towers):
        current = current + towers[current]
        return current

    def nth_stairs(self, n):
        if n == 0 or n == 1:
            return 1
        else:
            return self.nth_stairs(n - 1) + self.nth_stairs(n - 2)

    def countofstrings(self, a, b, c):
        if b < 0 or c < 0:
            return 0
        if a == 0:
            return 1
        if b == 0 and c == 0:
            return 1

        res = self.countofstrings(a - 1, b, c)
        res += self.countofstrings(a - 1, b - 1, c)
        res += self.countofstrings(a - 1, b, c - 1)

        return res

    def optimal_strategy(self, lst2, size):
        left_first = 0
        right_first = 0
        if size == 0:
            return 0
        else:
            for i in range(0, len(lst2)):
                if i % 2 == 0:
                    left_first += lst2[i]
                else:
                    right_first += lst2[i]

            '''
            if index < len(lst2):    
                if index % 2 == 0:
                    sum_left += lst2[index]
                else:
                    sum_right += lst2[index]
            return self.optimal_strategy(lst2, index + 1)'''
        print max(left_first, right_first)

    @staticmethod
    def negative_int_in_rows_cols(mat, rows, cols):
        count = 0
        i = 0
        j = cols - 1
        while j >= 0 and i < rows:
            if mat[i][j] < 0:
                count += (j + 1)
                i += 1
            else:
                j -= 1
        return count

    def cut_minimum_number_sqr(self, m, n, sum_):  # 30, 35
        if n == m:
            return 1

        temp = m

        if m != 0:
            sum_ += n / m
            m = n % m
            n = temp

            return self.cut_minimum_number_sqr(m, n, sum_)

        print sum_


if __name__ == '__main__':
    dp = DynamicProgramming()
    print dp.bytelandian_gold(12)

    lst = [[1, 2, 3],
           [4, 8, 2],
           [1, 5, 3]]
    print dp.min_cost_path(lst, 2, 2)

    dist = 4
    print(dp.printCountRec(dist))

    towers = [4, 2, 0, 0, 2, 0]
    print(dp.towerhopper(towers))

    print dp.sum_subset([3, 34, 4, 12, 5, 2], 9)
    print(dp.nth_stairs(4))
    print(dp.countofstrings(3, 1, 2))

    mat = [[-3, -2, -1, 1],
           [-1, 2, 3, 4],
           [4, 5, 7, 8]]
    rows = len(mat)
    cols = len(mat[0])
    print dp.negative_int_in_rows_cols(mat, rows, cols)

    print dp.cut_minimum_number_sqr(30, 35, 0)
