#!/usr/bin/env python3
# Thichanon Ratanasaenwan (Nont)
# 660510702
# Lab08_1
# 204111 Sec 002

def main():
    test()

def gcd(x, y):

    # absolute x และ y เพราะ gcd ไม่มีติดลบ
    x = abs(x)
    y = abs(y)

    # หลักคือการส่งเข้าฟังก์ชั่นเรื่อยๆจนกว่า y จะมีค่าเป็นศูนย์และ x ก็จะเป็นค่าของ gcd ที่ส่งออกจากฟังก์ชั่น
    # ถ้า y = 0
    if y == 0:
        # คืนค่า x
        return x
    else:
        #คืนค่า func ที่ส่ง y และ x mod y 
        return gcd(y, x % y)

def test():
    print(gcd(21, -7))
    print(gcd(-39, 78))

if __name__ == '__main__':
    main()