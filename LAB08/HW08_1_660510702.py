#!/usr/bin/env python3
# Thichanon Ratanasaenwan (Nont)
# 660510702
# HW08_1
# 204111 Sec 002

from math import isclose

def main():
    test_pi()
    # pass


def pi(n):

    # ฟังก์ชั่นคำนวนหาตัวหลัง
    def cal(x):
        if (x/2) % 2 == 0:
            return -(4 / (x * (x + 1) * (x + 2)))
        else:
            return (4 / (x * (x + 1) * (x + 2)))
        
    # ถ้า n = 0 
    if n == 0:
        # ให้คืนค่า 3
        return 3
    # ถ้า n != 0
    else:
        # ให้คืนค่าคำตอบ
        return pi(n-1) + cal(n*2)


def test_pi():
    epsilon = 10**-10
    assert isclose(pi(0), 3, abs_tol=epsilon)
    assert isclose(pi(1), 3.1666666666666665, abs_tol=epsilon)
    assert isclose(pi(2), 3.1333333333333333, abs_tol=epsilon)
    assert isclose(pi(5), 3.1427128427128426, abs_tol=epsilon)
    print("All OK!")
    


if __name__ == '__main__':
    main()
