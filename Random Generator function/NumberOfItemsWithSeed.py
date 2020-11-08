import random


def items_with_seed(num):
    nlist = [0, 1, 2, 3, 4, 5]
    random.seed(2)
    number_list = random.sample(nlist, num)
    return number_list
