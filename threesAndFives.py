def fives_n_threes(upper_bound):
    return sum(i for i in range(upper_bound) if (i % 3 == 0) or (i % 5 == 0))

print(fives_n_threes(1000))