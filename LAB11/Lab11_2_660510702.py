#!/usr/bin/env python3
# Thichanon Ratanasaenwan (Nont)
# 660510702
# Lab11_2
# 204111 Sec 002

def my_id():
    return "660510702"

def main():
    print(matching_sum((1,), 1))
    print(matching_sum((5, 2), 7))
    print(matching_sum((10, -1, 1, -8, 3, 1), 2))
    print(matching_sum((10, -1, 1, -8, 3, 1), 10))
    

def matching_sum(t, target_value):
    t = set(t)
    result = []

    for num in t:
        complement = target_value - num
        if complement in t:
            if num != 0 and complement != 0:
                result.append([num, complement])

    return(result)


if __name__ == '__main__':
    main()