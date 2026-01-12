def max_min_value(a, n):
    if len(a) == n:
        print(max(a))
        print(min(a))
        return max(a), min(a)


max_min_value([1, 100, 1000, 2, 2], 5)
