#!/usr/bin/env python3
# Thichanon Ratanasaenwan (Nont)
# 660510702
# HW06_2
# 204111 Sec 002

import string
def main():

    print(decode("aceiklmr-", '''
3 .
5 3 4 2 .
3 1 2 8 1 7 2 0 86 .
'''))


def decode_helper(code_table, str_index):  # รับรหัส 1 ตัว แล้วคืน 1 อักขระที่ถูกต้อง
    
    # ถ้า index เป็น "." ให้คืนค่า \n
    if str_index == '.':
        return '\n'
    
    # ถ้า index น้อยกว่าจำนวนตัวอักษร ให้คืนค่าตาม index
    elif str_index.isdigit() and int(str_index) < len(code_table):
        return code_table[int(str_index)]
    
    # ถ้า index น้อยกว่าหรือเท่ากับจำนวนตัวอักษรในค่าลบ ให้คืนค่าตาม index
    elif int(str_index) < 0 and int(str_index) >= (len(code_table)*-1):
        return code_table[int(str_index)]
    
    # ถ้า index มากกว่าให้คืนค่า "_"
    else:
        return '_'


def decode(code_table, text):
    # แยกรหัสทั้งหมด ให้กลายเป็น list เช่น ['3', '.', '5', '3', '4', '2', '.', ...]
    l_text = text.split()

    # เรียกใช้ฟังก์ชัน decode_helper() ที่มีหน้าที่รับรหัสหนึ่งตัว แล้วคืน 1 อักขระที่ถูกต้อง
    result_list = list(map(lambda x: decode_helper(code_table, x), l_text))
    
    # รวม list ของอักขระ ให้เป็น string
    result = ''.join(result_list)

    return result


if __name__ == '__main__':
    main()
