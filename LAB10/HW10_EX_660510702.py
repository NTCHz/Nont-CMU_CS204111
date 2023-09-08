#!/usr/bin/env python3
# Thichanon Ratanasaenwan (Nont)
# 660510702
# HW10_EX
# 204111 Sec 002

import string

cat = \
    '''
 ／|、    |
(°、。7   |
 |、 ~ヽ  |
 ᒐᒐ_f_ )ノ|
__________|
'''

def my_id():
    return "660510702"

def main():
    # test
    print(cat_altar(int(input())))

def cat_altar(n):

    # สร้าง list เก็บคำตอบ
    result = []
    # ตัว str ด้วย split 
    cat_O = cat.split("\n")

    # ลบ "|" ใน list
    for i in range(6):
        cat_p = cat_O[i]
        cat_p = cat_p[:-1]
        cat_O[i] = cat_p

    # ลบ " " ใน list
    cat_O = cat_O[1:-1]

    # หาโดยการทำทีละบรรทัดแล้ว append เข้าไปใน result
    for i in range(n):
        # หา space ด้านล่าง
        space_under= " "*(10*(2*i-1) + (2*i-2))
        for j in range(5):
            if i == 0:
                result.append(" "*11*(n-i-1) + cat_O[j])
                continue
            result.append(" "*11*(n-i-1) + cat_O[j] + "|" + space_under + "|" + cat_O[j])
    
    # ใช้ join ที่เป็น "\n" เพื่อที่จะเว้นบรรทัดของสมาชิกแต่ละตัวใน list
    result = "\n".join(result)

    # คืนค่า
    return result

if __name__ == '__main__':
    main()
