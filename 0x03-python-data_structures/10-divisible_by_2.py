#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    return [True for x in my_list if x % 2 == 0 else False]
    # return list(map(lambda x: True if x % 2 == 0 else False, my_list))
