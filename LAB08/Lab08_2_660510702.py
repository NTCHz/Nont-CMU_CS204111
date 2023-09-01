#!/usr/bin/env python3
# Thichanon Ratanasaenwan (Nont)
# 660510702
# Lab08_2
# 204111 Sec 002

def main():
    test()

def reverse_digits(x):

    # ตรวจว่า x < 0 ถ้าน้อยกว่า 0 ให้ส่ง abs x กลับไปในฟังก์ชั่นแล้วใส่ลบไว้ด้านหน้า
    if x < 0:
        return -(reverse_digits(abs(x)))
    
    # ตรวจว่า x เป็นเลข 0-9
    if x < 10 and x >= 0:
        return x
    
    # หาตัวสุดท้าย
    last = x % 10
    # หาตัวที่เหลือ
    remain = x // 10
    # คืนค่าแต่ละหลักบวกกัน
    return last * 10 ** (len(str(remain))) + reverse_digits(remain)

def test():
    print(reverse_digits(105506))

if __name__ == '__main__':
    main()