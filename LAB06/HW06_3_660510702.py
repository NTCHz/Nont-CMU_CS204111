#!/usr/bin/env python3
# Thichanon Ratanasaenwan (Nont)
# 660510702
# HW06_3
# 204111 Sec 002

def main():
    test()

def moving_average(list_a, w):
    # ถ้า w น้อยกว่า 0 และ w น้อยกว่าจำนวน list_a คืนค่า None
    if w <= 0 or w > len(list_a):
        return None

    # ฟังก์ชั่นหา avg 
    def moving_average_con(x):
        if x < len(list_a) and x+w < len(list_a)+1:
            window_sum = sum(list_a[x:x+w])
            return window_sum / w
    
    # การใช้ map + range หา avg ตามจำนวน w และขยับไปจนถึงตัวสุดท้ายโดยการใช้ func moving_average_con และเก็บไว้ใน list
    a = list(map(moving_average_con,range(0,len(list_a)-w+1)))

    # คืนค่า
    return a 

def test():
    print(moving_average([1, 2, 3, 4, 5], 2))
    print(moving_average([1, 2, 3, 4, 5], 3))
    print(moving_average([1, 2, 3, 4, 5], 4))

if __name__ == '__main__' :
    main()