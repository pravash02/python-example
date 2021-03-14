import copy


def get_minimum(k, a):
    print k, a
    if (k, a) in g:
        # Already calculated Set g[%d, (%s)]=%d' % (k, str(a), g[k, a]))
        return g[k, a]

    values = []
    all_min = []
    for j in a:
        set_a = copy.deepcopy(list(a))
        set_a.remove(j)
        all_min.append([j, tuple(set_a)])
        result = get_minimum(j, tuple(set_a))

        if result:
            print k, j
            values.append(matrix[k - 1][j - 1] + result)
    g[k, a] = min(values)
    print g[k, a]
    p.append(((k, a), all_min[values.index(g[k, a])]))

    return g[k, a]


if __name__ == '__main__':
    data = [1, 2, 3, 4]
    n = len(data)
    all_sets = []
    g = {}
    p = []
    matrix = [[0, 20, 42, 25],
              [20, 0, 30, 34],
              [42, 30, 0, 10],
              [25, 34, 10, 0]]

    for x in range(1, n):
        g[x + 1, ()] = matrix[x][0]

    get_minimum(1, (2, 3, 4))

    print('\n\nSolution to TSP: {1, ')
    solution = p.pop()
    print(solution[1][0])
    for x in range(n - 2):
        for new_solution in p:
            if tuple(solution[1]) == new_solution[0]:
                solution = new_solution
                print(solution[1][0])
                break
    print('1}')

