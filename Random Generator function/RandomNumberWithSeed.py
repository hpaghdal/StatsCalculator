import random
import numpy as np


def random_integer(num):
    nlist = (range(0, 9))
    random.seed(2)
    number_list = random.sample(nlist, num)
    return "Random integer is", number_list


print(random_integer(1))


def random_float(num):
    nlist = (np.arange(0.0, 9.0))
    random.seed(2)
    ran_float = random.uniform(nlist, num)
    return "Random float is", ran_float


print(random_float(1.0))
