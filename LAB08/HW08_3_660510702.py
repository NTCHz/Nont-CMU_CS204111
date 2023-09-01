#!/usr/bin/env python3
# Thichanon Ratanasaenwan (Nont)
# 660510702
# HW08_3
# 204111 Sec 002

import string
def main():
    test()

def is_anagram(s1, s2):
    
    # กรณีที่เป็นช่องว่าง และ เป็น int
    if s1 == ' ' or s2 == ' ' or type(s1) == int or type(s2) == int:
        return False
    
    # แปลงเป็นตัวพิมพ์เล็กทั้งสองสตริง
    s1 = s1.lower()
    s2 = s2.lower()
    
    # กรองอักขระที่ไม่ใช่ตัวอักษร
    s1 = ''.join(filter(str.isalpha, s1))
    s2 = ''.join(filter(str.isalpha, s2))
    
    # ถ้าความยาวของสตริงไม่เท่ากัน ไม่ใช่อะนาแกรม
    if len(s1) != len(s2):
        return False
    
    # ถ้าสตริงเป็นสตริงว่างทั้งคู่ ถือว่าเป็นอะนาแกรม
    if len(s1) == 0:
        return True
    
    # เปรียบเทียบตัวอักษรแรกของ s1 กับทั้ง s2
    if s1[0] in s2:
        # หาตำแหน่งของตัวแรกใน s2
        index = s2.index(s1[0])
        # ตรวจสอบ str ที่เหลือ
        return is_anagram(s1[1:], s2[:index] + s2[index+1:])
    else:
        return False


def test():
    print(is_anagram("Tom Marvolo Riddle", "I am Lord Voldemort!!!"))
    print(is_anagram("cat", "tab"))
    print(is_anagram("Nissan", "Insacne"))
    print(is_anagram("Eleven plus two", "Twelve plus one"))
    print(is_anagram(" ", " "))
    print(is_anagram(1,1))
    print(is_anagram("T T T", "T"))

if __name__ == '__main__' :
    main()
    