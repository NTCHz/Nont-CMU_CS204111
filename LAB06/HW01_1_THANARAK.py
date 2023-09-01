#!/usr/bin/env python3
# Thichanon Ratanasaenwan (Nont)
# 660510702
# HW06_1
# 204111 Sec 002

import string

def main():
    test()


def uniform(line):

    uppercase_ = list(filter(lambda x: x.isupper(), line))
    count_uppercase = len(uppercase_)

    print(count_uppercase)


def test():

    # assert(uniform('HaPpY')) == 'HAPPY'
    # assert(uniform('cOdINg')) == 'coding'
    # assert(uniform('coMP scI!!!')) == 'comp sci!!!'
    # print("All OK")

    uniform('HaPpY')

if __name__ == '__main__':
    main()