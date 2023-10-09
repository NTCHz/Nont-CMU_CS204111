#!/usr/bin/env python3 
# Thichanon Ratanasaenwan (Nont)
# 660510702
# HW14_3
# 204111 Sec 002

import copy

def main():
    list_x = ['beer', 'wine', 'vinegar', 'vodka'] 
    radix_word(list_x, True) 
    print('--------') 
    print(list_x) 

def my_id():
    return "660510702"

def radix_word(list_x, show_steps=False):
    n = len(list_x)
    list_copy = copy.deepcopy(list_x)
    max_length = max(len(s) for s in list_x)
    

    for i in range(max_length-1 ,-1,-1):
        for j in range(n):
            list_x[j] += " "*(max_length - len(list_x[j]))

        list_x = sorted(list_x, key=lambda x: x[i])

        for k in range(n):
            list_x[k] = list_x[k].replace(" ", "")

        if show_steps:
            print(list_x)

    for k in range(n):
        list_x[k] = list_x[k].replace(" ", "")

    print
    

if __name__ == "__main__":
    main()