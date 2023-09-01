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
    
    if len(list_a) == 0:
        gold_list = []
        silver_list = []
        bronze_list = []
        return (tuple([gold_list, silver_list, bronze_list]))
    
    max_list_a = max(list_a)
    max_len_list_a = list_a.count(max_list_a)
    
    if len(list_a) == 1:
        gold_list = [max_list_a] * max_len_list_a
        silver_list = []
        bronze_list = []
        return (tuple([gold_list, silver_list, bronze_list]))

    new_list = list(map(lambda x: None if x == max_list_a else x, list_a))
    new_list = list(filter(lambda x: x is not None, new_list))
    
    if max_len_list_a < 3:
        if len(new_list) != 0:
            new_max_list_a = max(new_list)
            new_max_len_list_a = list_a.count(new_max_list_a)
            if new_max_list_a == 0:
                gold_list = [max_list_a] * max_len_list_a
                silver_list = [0]
                bronze_list = []
                return (tuple([gold_list, silver_list, bronze_list]))
            
            if new_max_len_list_a == 2 and max_len_list_a != 2:
                gold_list = [max_list_a] * max_len_list_a
                silver_list = [new_max_list_a] * new_max_len_list_a
                bronze_list = []
                return (tuple([gold_list, silver_list, bronze_list]))

            else:  

                new_list = list(map(lambda x: None if x == new_max_list_a else x, new_list))
                new_list = list(filter(lambda x: x is not None, new_list))
                
                if len(new_list) != 0:
                    newer_max_list_a = max(new_list)
                    newer_max_len_list_a = list_a.count(newer_max_list_a)

                    if new_max_list_a == 0 and max_len_list_a != 2:
                        gold_list = [max_list_a] * max_len_list_a
                        silver_list = [new_max_list_a] * new_max_len_list_a
                        bronze_list = []
                        return (tuple([gold_list, silver_list, bronze_list]))
                    
                    else:
                        if max_len_list_a == 2:
                            gold_list = [max_list_a] * max_len_list_a
                            silver_list = []
                            bronze_list = [new_max_list_a] * new_max_len_list_a
                            return (tuple([gold_list, silver_list, bronze_list]))

                        else:
                            gold_list = [max_list_a] * max_len_list_a
                            silver_list = [new_max_list_a] * new_max_len_list_a
                            bronze_list = [newer_max_list_a] * newer_max_len_list_a
                            return (tuple([gold_list, silver_list, bronze_list]))
                else:
                    gold_list = [max_list_a] * max_len_list_a
                    silver_list = [new_max_list_a] * new_max_len_list_a
                    bronze_list = []
                    return (tuple([gold_list, silver_list, bronze_list]))
        else:
            gold_list = [max_list_a] * max_len_list_a
            silver_list = []
            bronze_list = []
            return (tuple([gold_list, silver_list, bronze_list]))

    else:
        gold_list = [max_list_a] * max_len_list_a
        silver_list = []
        bronze_list = []
        return (tuple([gold_list, silver_list, bronze_list]))


def test():
    print(medal_allocation([9, 8, 8, 7, 6, 5, 4, 3, 2]))
    print(medal_allocation([9, 8, 7, 7, 6, 5, 4, 3, 2]))
    print(medal_allocation([9, 9, 8, 7, 6, 5, 4, 3, 2]))
    print(medal_allocation([9, 9, 9, 8, 7, 6, 5, 4, 3, 2]))
    print(medal_allocation([5,4]))
    print(medal_allocation([5]))
    print(medal_allocation([5, 7, 8, 2, 7, 1]))
    print(medal_allocation([9, 9, 9, 9, 8, 7, 6, 5, 4, 3, 2]))
    print(medal_allocation([]))
    print(medal_allocation([4,5,0]))
    # print(medal_allocation([]))


    

if __name__ == '__main__' :
    main()