#!/usr/bin/env python3
# Thichanon Ratanasaenwan (Nont)
# 660510702
# HW04_1
# 204111 Sec 002

def main():
    # รับค่า
    p = int(input())
    c = int(input())

    # เรียกใช้ฟังก์ชั่น
    print(calculate_p2p_evolve_exp(p, c))


def calculate_p2p_evolve_exp(p, c):
    # ถ้าไม่มี candy และมีไม่ถึง 12 ตัว จะไม่สามารถ evo ได้
    if c == 0 and p < 12:
        return 0
    
    # ถ้า จำนวนตัวน้อยกว่าจำนวนที่ evo ได้ จะสามารถ evo ได้แค่ตัวเดียว
    if p < (p + c - 2)//11:
        return p * 500
    
    # จำนวนที่สามารถ evo ได้ โดยการนับ pidgey เป้ฯหนึ่งแคนดี้แต่ไม่สามารถนับตัวแรกและตัวสุดท้ายได้ จึงนำไปลบสอง และนำไปหาร 11 เพราะ ตอน evole จะได้ candy กลับมา 1 อัน แล้วนำไปคูร 500 เพื่อหา exp
    else:
        a = (p + c - 2)//11 * 500
    return a 

if __name__ == '__main__':
    main()
