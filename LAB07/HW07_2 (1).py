#!/usr/bin/env python3
# Thiwat Thachumpu
# 660510652
# HW07_2
# 204111 Sec 002

def main():
    print(medal_allocation([0, 0, 0, 0]))
    print(medal_allocation([9, 9, 8, 7, 6, 5, 4, 3, 2]))
    print(medal_allocation([9, 9, 8, 8, 7, 6, 5, 4, 3, 2]))
    resuit_list = [[], [], []]
    resuit_tuple = tuple(resuit_list)
    print(resuit_tuple)
    # test()
    pass

def medal_allocation(list_a):
    total = 0
    resuit_list = [[], [], []]
    sort_list = sorted(list_a, reverse=True)
    


    #Gold medel 
    if sort_list[0] <= 0:
        return tuple(resuit_list)
    st = sort_list.count(sort_list[0])
    resuit_list[0] = (sort_list[0:st])
    total += st


    # Silver medal 
    if total <3:
        if sort_list[st] <= 0:
            return tuple(resuit_list)
        nd = sort_list.count(sort_list[st])
        resuit_list[total] = (sort_list[st:st+nd])
        total += nd


    #  Bronze medal
    if total < 3:
        if sort_list[st+nd] <= 0:
            return tuple(resuit_list)
        rd = sort_list.count(sort_list[st +nd])
        resuit_list[total] = (sort_list[st+nd:st+nd+rd])

    resuit_tuple = tuple(resuit_list)
    return resuit_tuple


def test():
    # assert medal_allocation([9, 9, 9, 9, 8, 7, 6, 5, 4, 3, 2]) == ([9, 9, 9, 9], [], [])
    # assert medal_allocation([9, 9, 8, 7, 6, 5, 4, 3, 2]) == ([9, 9], [], [8])
    # assert medal_allocation([0, 0, 0, 0]) == ([], [], [])
    print(medal_allocation([9, 9, 8, 7, 6, 5, 4, 3, 2]))
    print('pass')

if __name__ =='__main__':
    main()