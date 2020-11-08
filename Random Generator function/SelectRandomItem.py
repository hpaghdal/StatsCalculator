import random


def random_item(num):
    nList = [0, 1, 2, 3, 4, 5]
    numbered_list = random.sample(nList, num)
    return "random item", numbered_list


print(random_item(1))