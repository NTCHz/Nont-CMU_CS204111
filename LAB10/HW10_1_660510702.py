#!/usr/bin/env python3
# Thichanon Ratanasaenwan (Nont)
# 660510702
# HW10_1
# 204111 Sec 002


def my_id():
    return "660510702"

def main():
    result = eratosthenes(100, True)     
    print('----') 
    print(result)

    # result = eratosthenes(20)     
    # print('----') 
    # print(result)

def eratosthenes(n, show_step=False):
    
    # สร้าง list ตั้งแต่ 2 ถึง n
    numbers = list(range(2,n+1))

    prime_n = []

    while numbers:

        # กำหนด prime เป็นตัวแรก
        prime = numbers[0]
        # เก็บค่า prime ไว้ใน prime_n
        prime_n.append(prime)
        # ลบตัวเลขที่หารด้วยจำนวน prime ได้
        numbers = [num for num in numbers if num % prime != 0]
        # ถ้า prime * prime น้อยกว่าเท่ากับ n
        if prime * prime <= n:
            # ถ้า show_step == True
            if show_step:
                # ให้แสดงค่า
                print(f'{prime}: {prime_n + numbers}')
                
    # คืนค่า
    return prime_n

if __name__ == '__main__':
    main()