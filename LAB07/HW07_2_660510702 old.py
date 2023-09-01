#!/usr/bin/env python3
# Thichanon Ratanasaenwan (Nont)
# 660510702
# HW07_2
# 204111 Sec 002

def main():
    test()

def medal_allocation(list_a):
    
    def del_list_a(score):
        list_a.remove(score)

    max_score = max(list_a)
    max_score_count = list_a.count(max_score)

    list(map(lambda x: del_list_a(max_score),range(1,max_score_count+1)))

    new_max_score = max(list_a)
    new_max_score_count = list_a.count(new_max_score)

    list(map(lambda x: del_list_a(new_max_score),range(1,new_max_score_count+1)))

    newer_max_score = max(list_a)
    newer_max_score_count = list_a.count(newer_max_score)

    list(map(lambda x: del_list_a(newer_max_score),range(1,newer_max_score_count+1)))

    
    if max_score_count == 2:
        newer_max_score_count = max_score

    if max_score_count >= 3:
        new_max_score_count = 0
        newer_max_score_count = 0

    if new_max_score_count == 0:
        sum_str_count = (str(max_score) * max_score_count) + (str(new_max_score) * newer_max_score_count) + (str(newer_max_score) * new_max_score_count)
        # print(1)
    else:
        sum_str_count = (str(max_score) * max_score_count) + (str(new_max_score) * new_max_score_count) + (str(newer_max_score) * newer_max_score_count)

    # print(sum_str_count)
    # sum_str_count = (str(max_score) * max_score_count) + (str(new_max_score) * new_max_score_count) + (str(newer_max_score) * newer_max_score_count)
    if len(sum_str_count) > 5:
        sum_str_count = sum_str_count[:-(len(sum_str_count)-5)]

    list_s = list(sum_str_count)
    list_s = list(map(lambda x: int(x),list_s))

    count_gold = list_s.count(max_score)
    count_silver = list_s.count(new_max_score)
    count_bronze = list_s.count(newer_max_score)

    gold_list = [max_score] * count_gold
    if count_gold == 2:
        silver_list = [new_max_score] * 0
        bronze_list = [new_max_score] * count_silver
    else:
        silver_list = [new_max_score] * count_silver
        bronze_list = [newer_max_score] * count_bronze

    print (tuple([gold_list, silver_list, bronze_list]))


def test():
    medal_allocation([9, 9, 8, 8, 8, 8, 7, 6, 5, 4, 3, 2])
    medal_allocation([9, 8, 7, 7, 7, 7, 7, 3, 2])
    medal_allocation([9, 9, 8, 7, 6, 5, 4, 3, 2])
    medal_allocation([9, 9, 9, 9, 8, 7, 6, 5, 4, 3, 2])
    medal_allocation([9])

if __name__ == '__main__' :
    main()