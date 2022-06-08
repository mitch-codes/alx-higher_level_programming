#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    list_uniq = []
    uniq = set(my_list)
    for number in uniq:
        list_uniq.append(number)
    for i in range(len(list_uniq)):
        sum = sum + list_uniq[i]
    return sum
