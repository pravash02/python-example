def smallest_non_constructible_value(A):
    max_constructible = 0
    for a in sorted(A):
        if a > max_constructible + 1:
            break
        max_constructible += a
    return max_constructible + 1


if __name__ == "__main__":
    array = [1, 2, 4]

    print(smallest_non_constructible_value(array))
