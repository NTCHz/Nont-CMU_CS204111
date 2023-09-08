#!/usr/bin/env python3
# Thichanon Ratanasaenwan (Nont)
# 660510702
# Lab10_2
# 204111 Sec 002


def my_id():
    return "660510702"

def main():
    print(longest_digit_run(11777332))
    print(longest_digit_run(1177332))

def longest_digit_run(n):
    # แปลงเป็น str
    n = str(n)
    # กำหนดตัวแปรจำนวนสูงสุด จำนวนสูงสุดนับปัจจุบัน str ตัวแรก
    max_l = 0
    cur_l = 1
    pre_digit = n[0]

    for digit in n[1:]:
        if digit == pre_digit:
            cur_l +=1
        else:
            # ถ้าพบตัวเลขที่ไม่ติดกันกับตัวเลขก่อนหน้า
            # จะเทียบความยาวปัจจุบันกับตอนแรก แล้วแทยด้วยจำนวนสูงสุด
            if cur_l > max_l:
                max_l = cur_l
            cur_l = 1
            pre_digit = digit

    # ตรวจสอบกรณีสุดท้าย
    if cur_l > max_l:
        max_l = cur_l

    # คืนค่า
    return max_l
            
        
    
if __name__ == '__main__':
    main()