#!/usr/bin/env python3
# Thichanon Ratanasaenwan (Nont)
# 660510702
# HW08_2
# 204111 Sec 002

def main():
    test()

def base_b(x, b):

    if x < b:
        return x
    
    return base_b(x // b, b) * 10 + (x % b)

def test():
    print(base_b(-8, 2))
    print(base_b(11, 3))

if __name__ == '__main__' :
    main()
    
