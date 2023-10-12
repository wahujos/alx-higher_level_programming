#!/usr/bin/python3
def weight_average(my_list=[]):
    sum_total = 0
    divisor = 0
    if not my_list:
        return 0
    else:
        for tup in my_list:
            mul = tup[0] * tup[1]
            sum_total += mul
            divisor += tup[1]
            average = sum_total / divisor
        return average
