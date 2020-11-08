import random


def randomly_same(num):
    nlist = [0, 1, 2, 3, 4, 5]
    random.seed(2)
    number_list = random.sample(nlist, num)
    return number_list
