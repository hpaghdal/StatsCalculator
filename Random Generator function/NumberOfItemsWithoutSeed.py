import random


def items_without_seed(num):
    nlist = [0, 1, 2, 3, 4, 5]
    number_list = random.sample(nlist, num)
    return number_list
