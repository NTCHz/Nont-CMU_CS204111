#!/usr/bin/env python3
# Thichanon Ratanasaenwan (Nont)
# 660510702
# HW06_1
# 204111 Sec 002

import string

def main():
    test()


def uniform(line):

    # ฟังก์ชั่นแยกตัวพิมพ์ใหญ่
    def check_upper(x):
        if x in string.ascii_uppercase:
            return True
        
    # ฟังก์ชั่นแยกตัวพิมพ์เล็ก
    def check_lower(x):
        if x in string.ascii_lowercase:
            return True

    #เรียกใช้ func โดนการใช้ filter ในการแยก
    upper = list(filter(check_upper, line))
    lower = list(filter(check_lower, line))

    # เทียบจำนวนระหว่างตัวพิมพ์ใหญ่กับตัวพิมพ์เล็ก
    if len(upper) < len(lower):
        return str.lower(line)
    elif len(upper) > len(lower):
        return str.upper(line)
    else:
        # ในกรณีที่เท่ากันให้ดูตัวหน้า โดยการหาว่าตัวแรกของ line เป็นตัวพิมพ์เล็กหรือใหญ่
        if line[0] in string.ascii_uppercase:
            return str.upper(line)
        else:
            return str.lower(line)


def test():

    assert(uniform('HaPpY')) == 'HAPPY'
    assert(uniform('cOdINg')) == 'coding'
    assert(uniform('coMP scI!!!')) == 'comp sci!!!'
    print("All OK")

if __name__ == '__main__':
    main()