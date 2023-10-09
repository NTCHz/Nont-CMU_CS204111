#!/usr/bin/env python3 
# Thichanon Ratanasaenwan (Nont)
# 660510702
# LAB15_1
# 204111 Sec 002

def main():
    print(sum_nested_list([1, 2, [[3, [[4], 5]], [6, 7]]])) 
    print(sum_nested_list([1, [2, [3]]])) 
    print(sum_nested_list([1, [[2, [3]], 4, [5]], [6, [7]]])) 
    print(sum_nested_list([9, [[8, [7]], 6, [5, [44, [33]]]]])) 

def my_id():
    return "660510702"

def sum_nested_list(list_a, depth=1):
    total = 0
    for i in list_a:
        if isinstance(i, int):
            total += i * depth
        elif isinstance(i, list):
            total += sum_nested_list(i, depth + 1)
            
    return total

if __name__ == '__main__':
    main()