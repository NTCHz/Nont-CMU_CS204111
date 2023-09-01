#!/usr/bin/env python3
# Thichanon Ratanasaenwan (Nont)
# 660510702
# HW05_1
# 204111 Sec 002

import string

def main():
    test_palindrome_without()


# implement this function
def palindrome_without(text, c):
    
    # แปลงทุกตัวเป็นตัวพิมพ์เล็ก
    text = str.lower(text)

    # แทนที่ตัวต้องการลบ และช่องว่าง
    a = text.replace(c, "").replace(" ", "")

    # ส่งค่า boolean กลับ โดยมีเงื่อนไขว่า ข้อความเมื่อกลับข้อความแล้วต้องเหมือนกัน และจำนวนข้อความต้องไม่เท่ากับ 0
    return a == a[::-1] and len(a) != 0 

# test function
def test_palindrome_without():

    assert(palindrome_without("Banana", "b")) == True
    assert(palindrome_without("Swap of paws", "f")) == True
    assert(palindrome_without("T", "t")) == False

if __name__ == "__main__":
    main()
