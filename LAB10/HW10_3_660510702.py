#!/usr/bin/env python3
# Thichanon Ratanasaenwan (Nont)
# 660510702
# HW10_3
# 204111 Sec 002

def my_id():
    return "660510702"

def main():
    # print(polynomial_addition([(2, 6), (1, 34), (0, -1)], [(2, -6), (0, 8), (1, 1)]))
    # print(polynomial_addition([(2, -6), (0, 2), (1, 1)],[(0, -8),(2, -6)]))
    print(polynomial_addition([(3, -6), (3, 2), (1, 1)],[(0, -8),(2, -6)]))


def polynomial_addition(p1, p2):
    
    merged_p = p1 + p2
    result = []
    
    # ใช้ sorted() 
    merged_sorted = sorted(merged_p, key=lambda x: x[0], reverse=True)
    
    # เริ่มต้นจากกำลังสูงสุด
    max_power = merged_sorted[0][0]
    cur_coefficient = 0
    
    for power, coefficient in merged_sorted:
        if power == max_power:
            # รวมสัมประสิทธิ์เดียวกัน
            cur_coefficient += coefficient
            
        else:
            # เพิ่มค่า ยกเว้นตัวที่เป็น 0
            if cur_coefficient != 0:
                result.append((max_power, cur_coefficient))
            
            # รีเซ็ตค่าสัมประสิทธิ์และกำลัง
            max_power = power
            cur_coefficient = coefficient
    
    # เพิ่มค่าสุดท้าย ยกเว้นตัวที่เป็น 0
    if cur_coefficient != 0:
        result.append((max_power, cur_coefficient))

    # คืนค่า
    return result


if __name__ == '__main__' :
    main()


