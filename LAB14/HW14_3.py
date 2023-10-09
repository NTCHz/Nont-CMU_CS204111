#!/usr/bin/env python3 
# Thichanon Ratanasaenwan (Nont)
# 660510702
# HW14_3
# 204111 Sec 002

def main():
    list_x = ['beer', 'wine', 'vinegar', 'vodka'] 
    radix_word(list_x, True) 
    print('--------') 
    print(list_x) 

    list_x = ['beer', 'wine', 'vinegar', 'vodka'] 
    radix_word(list_x) 
    print('--------') 
    print(list_x)

def my_id():
    return "660510702"

def radix_word(list_x, show_steps=False):

    max_length = max(len(s) for s in list_x)

    for position in range(max_length - 1, -1, -1):
        n = len(list_x)
        result = [0] * n
        count = [0] * 256

        for i in range(n):
            idx = ord(list_x[i][position]) if position < len(list_x[i]) else 0
            count[idx] += 1

        for i in range(1, 256):
            count[i] += count[i - 1]

        i = n - 1
        while i >= 0:
            idx = ord(list_x[i][position]) if position < len(list_x[i]) else 0
            result[count[idx] - 1] = list_x[i]
            count[idx] -= 1
            i -= 1
        
        for i in range(n):
            list_x[i] = result[i]

        if show_steps:
            print(list_x)

if __name__ == "__main__":
    main()