__author__ = 'zhangxa'

from collections import defaultdict

MAX_INT = 9
STR_LIST = ['ABC','BCA']

def calc_weight(str,dict):
    """
    caculate the weight of every letter and store it in dict.
    the weight will be higher of the letter in the front of the str.
    :param str:
    :param dict:
    :return:
    """
    for i,c in enumerate(str):
        dict[c] += 10**(len(str)-(i+1))

#cacuclate the weights by traverse the STR_LIST
dict = defaultdict(int)
for str in STR_LIST:
    calc_weight(str,dict)

#sort the dict by weights and return a list like ['B','A','C']
sort_weights = sorted(dict.keys(),key=lambda k:dict[k],reverse=True)

#define which char's weight will be lowest
def adjust_sort_weights(sort_weights,str_lst):
    zero_index = -1
    for i in range(len(sort_weights),0,-1):
        index = i - 1
        c = sort_weights[index]
        bFind = True
        for str in str_lst:
            if c == str[0]:
                bFind = False
                break
        if bFind:
            zero_index = index
            break
    if zero_index == -1:
        raise RuntimeError("can't find a char to be mapped zero")
    else:
        sort_weights.append(sort_weights[zero_index])
        del sort_weights[zero_index]
    return zero_index

print(sort_weights[adjust_sort_weights(sort_weights,STR_LIST)])

def caculate_sum(sort_weights,str_lst):
    sum = 0
    for str in str_lst:
        int_str = ''
        for i,c in enumerate(str):
            int_str = '%s%s'%(int_str,MAX_INT-sort_weights.index(c))
        sum += int(int_str)
    return sum

print(caculate_sum(sort_weights,STR_LIST))
