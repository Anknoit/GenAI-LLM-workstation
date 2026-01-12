# Analysis of algorithms is the determination of the amount of time and space resources required to execute it

# IP = 3
# OP = 6


# IP = 5
# OP = 15

# 1st Method

my_list = []


def sum_fact(n):
    for i in range(1, n + 1):
        # i = i+1
        print(i)
        my_list.append(i)
    print("Sum of n values = ", sum(my_list))
    return i


sum_fact(3)

# 2nd Method


def sum_second(n):
    a = 0
    for i in range(1, n + 1):
        # for j in i:
        # variable rotation
        # a = j[i]
        # b = [j + 1]
        # c = a + b
        # a = b
        # b = c
        a = a + i
    print(a)
    return a


sum_second(5)


# 3rd Method
def sum_third(n):
    print(n * ((n + 1) / 2))


sum_third(6)


# 4th Method - WRONG WHY BITCH???
def sum_fourth(n):
    a = 0
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            a = a + j
    print("Fourth method n =", a)


n = 3
sum_fourth(n)
