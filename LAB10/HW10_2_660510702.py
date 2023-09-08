#!/usr/bin/env python3
# Thichanon Ratanasaenwan (Nont)
# 660510702
# HW10_2
# 204111 Sec 002

import string
    
def my_id():
    return "660510702"

def main():
    print(unmask_id('*-2345-67890-*1-*'))
    # unmask_id('1-2345-6789*-*1-1')
    # unmask_id('1-2345-67*90-*1-*')

def unmask_id(masked_id):
    # นับจำนวน star หรือ "*"
    num_stars = masked_id.count('*')
    
    # สร้าง list ที่เก็บคำตอบ
    possible_ids = []

    # func Check
    def Check(citizen_id):
        # แทน - เป็น ""
        citizen_id = citizen_id.replace("-","")
        # เช็คความยาว ตัวเลข และตัวแรกต้องไม่เป็น 0
        if len(citizen_id) != 13 or not citizen_id.isdigit() or citizen_id[0] == '0':
            return False
    
        total = 0
        # เช็คตาม algorithm จาก https://memo8.com/check-digit-thai-citizen-id-validator/
        for i in range(12):
            total += int(citizen_id[i]) * (13 - i)
        remainder = total % 11
        check_digit = (11 - remainder) % 10

        # คืนค่า
        return int(citizen_id[12]) == check_digit
    
    # func เติมตัวเลขลงที่ star หรือ "*"  
    for i in range(10 ** num_stars):
        id_str = str(i).zfill(num_stars)
        # แทน "*" ด้วย {}
        unmasked_id = masked_id.replace('*', '{}', num_stars)
        # แทน {} ด้วย id_star โดยใช้ format
        full_id = unmasked_id.format(*id_str)

        # ส่งไปตรวจสอบว่าเป็นจริงหรือมั้ยใน func Check
        if Check(full_id):
            possible_ids.append(full_id)

    # คืนค่า
    return possible_ids


if __name__ == '__main__':
    main()