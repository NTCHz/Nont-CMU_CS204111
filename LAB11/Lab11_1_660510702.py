#!/usr/bin/env python3
# Thichanon Ratanasaenwan (Nont)
# 660510702
# Lab11_1
# 204111 Sec 002

import string

def my_id():
    return "660510702"

def main():
    print(word_count("He doesn't want to pay $40,000 for a new car, but his wife doesn't seem to care."))
    # print(word_count("This is a sample text.. This text contains some words. Words are important in this text."))

def word_count(text):

    # สร้าง list ที่ลบเครื่องหมายวรรคตอนออก เฉพาะที่ล้อมรอบคำ
    list_a = []

    # เปลี่ยนเป็นพิมพ์เล็ก
    text = text.lower()
            
    # แยกแต่ละคำใส่ใน list
    words = text.split()

    # ลบเครื่องหมายวรรคตอนออก
    for w in words:
        w = w.strip(string.punctuation)
        list_a.append(w)
                
    # สร้าง dict
    words_freq = {}

    '''
    เงื่อนไขในการ add ลงไปใน dict โดยการที่เช็คว่ามี key ตัวไหนที่เหมือนถ้าเหมือนให้ Value += 1
    แต่ถ้าไม่เหมือนให้ add ลงไปใน dict แล้ว กำหนด Value เป็น 1 
    '''
    for word in list_a:
        if word in words_freq:
            words_freq[word] += 1
        else:
            words_freq[word] = 1

    # คืนค่า
    return words_freq


if __name__ == '__main__':
    main()