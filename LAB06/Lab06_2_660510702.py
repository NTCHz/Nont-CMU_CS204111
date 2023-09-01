#!/usr/bin/env python3
# Thichanon Ratanasaenwan (Nont)
# 660510702
# Lab06_2
# 204111 Sec 002

def main():
    test()

def dest_rotate_list(list_a, n):

    # mod จำนวนด้วยความยาวของ list
    n %= len(list_a)

    # rotate โยใช้ การ copy list โดยไม่ยุ่งกับ list เดิม
    list_a[:] = list_a[-n:] + list_a[:-n]


def test():
    pass
    # assert(dest_rotate_list([1, 2, 3, 4], 1)) == [4, 1, 2, 3]
    # assert(dest_rotate_list([1, 2, 3, 4], 105)) == [4, 1, 2, 3]
    # assert(dest_rotate_list([1, 2, 3, 4], -1)) == [2, 3, 4, 1]
    # print("ALL OK")
    # dest_rotate_list([1, 2, 3, 4], 1)
    # dest_rotate_list([1, 2, 3, 4], 105)
    # dest_rotate_list([1, 2, 3, 4], -1)


if __name__ == '__main__' :
    main()
