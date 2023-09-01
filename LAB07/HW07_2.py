#!/usr/bin/env python3
# Thichanon Ratanasaenwan (Nont)
# 660510702
# HW07_2
# 204111 Sec 002

def main():
    test()

def medal_allocation(list_a):

    list_a = sorted(list_a, reverse=True)
    list_a = list_a[:5]

    result_total = 0
    result = [[],[],[]]

    if len(list_a) == 0 or list_a[0] == 0:
        return tuple([[], [], []])
    
    if len(list_a) != 0:
        if list_a[0] > 0:
            count_max = list_a.count(list_a[0])
            result[0] = ([list_a[0]]*count_max)
            result_total += count_max
            if result_total >= 3:
                return tuple(result)
    
    list_a = list(filter(lambda x: x is not list_a[0], list_a))
    
    if len(list_a) != 0:
        if list_a[0] > 0 and result_total != 2 and result_total < 3:
            count_max = list_a.count(list_a[0])
            result[1] = ([list_a[0]]*count_max)
            result_total += count_max
        else:
            if result_total == 2:
                result[1] = []
                result[2] = [list_a[0]]
            else:
                result[1] = []

    list_a = list(filter(lambda x: x is not list_a[0], list_a))

    if len(list_a) != 0 and result[2] == []:
        if list_a[0] > 0 and result_total < 3:
            count_max = list_a.count(list_a[0])
            result[2] = ([list_a[0]]*count_max)
            result_total += count_max
        else:
            result[2] = []

    return tuple(result)


def test():
    # print(medal_allocation([9, 8, 8, 7, 6, 5, 4, 3, 2]))
    # print(medal_allocation([9, 8, 7, 7, 6, 5, 4, 3, 2]))
    # print(medal_allocation([9, 9, 8, 7, 6, 5, 4, 3, 2]))
    # print(medal_allocation([9, 9, 9, 8, 7, 6, 5, 4, 3, 2]))
    # print(medal_allocation([5,4]))
    # print(medal_allocation([5]))
    # print(medal_allocation([5, 7, 8, 2, 7, 1]))
    # print(medal_allocation([9, 9, 9, 9, 8, 7, 6, 5, 4, 3, 2]))
    # print(medal_allocation([]))
    # print(medal_allocation([4,5,0]))
    print(medal_allocation([9, 9, 8, 7, 6, 5, 4, 3, 2]))


    

if __name__ == '__main__' :
    main()