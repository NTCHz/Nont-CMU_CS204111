#!/usr/bin/env python3
# Thichanon Ratanasaenwan (Nont)
# 660510702
# HW05_2
# 204111 Sec 002

import string

def main():
    test_rotate()


# implement this function
def rotate(num, pos):
    num = str(num)
    if pos <= 5 and pos >= -5:
        return int(num[0-pos:] + num[:0-pos]) 
    else:
        if pos < 0:
            # print(pos)
            pos = abs(pos) % 5
            if pos == 0:
                pos = 5
            # print(pos)
            pos = 0-pos
            return int(num[0-pos:] + num[:0-pos])
            
        else:   
            pos = abs(pos) % 5
            if pos == 0:
                pos = 5
            # print(pos)
            return int(num[0-pos:] + num[:0-pos])

    

# test function
def test_rotate():

    assert(rotate(12345, 3)) == 34512
    assert(rotate(12345, 2)) == 45123
    assert(rotate(12345, -3)) == 45123
    assert(rotate(12345, -103)) == 45123
    # print(rotate(12345, -106))


if __name__ == "__main__":
    main()
