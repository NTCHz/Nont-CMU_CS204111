#!/usr/bin/env python3
# Thichanon Ratanasaenwan (Nont)
# 660510702
# Lab10_1
# 204111 Sec 002


def my_id():
    return "660510702"

def main():
    print(comma_separated(3400,3))
    print(comma_separated(3400,4))
    print(comma_separated(781588,5))
    print(comma_separated(1234))
    print(comma_separated(1000000))

def comma_separated(n, digit=3):
    # แปลงเป็น str
    n = str(n)
    # ถ้า digit มากกว่าจำนวน n ให้คืนค่าเดิม
    if digit >= len(n):
        return n 
    
    # กลับด้าน str
    n = n[::-1]
    # กำหนดตัวแปร
    r = ""
    i = 0

    # ถ้า i น้อยกว่าหรือเท่ากับจำนวน str(n) - 1 
    while i <= len(n)-1:
        # ถ้า i mod digit แล้วเป็นศูนย์ให้เติม ','
        if i % digit == 0:
            r += "," 

        # ให้ตัวแปร r เก็บตัวอักษร
        r += n[i]

        i += 1

    # กลับด้าน str
    r = r[:len(r)-1:-1]
    # ตัดตัวท้ายออก
    r = r[:len(r)-1]
    
    # คืนค่า
    return r
    

        

if __name__ == '__main__':
    main()