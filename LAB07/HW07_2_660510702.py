#!/usr/bin/env python3
# Thichanon Ratanasaenwan (Nont)
# 660510702
# HW07_2
# 204111 Sec 002

def main():
    test()

def medal_allocation(list_a):

    # เรียงลำดับใน list
    list_a = sorted(list_a, reverse=True)

    # กำหนดจำนวนคำตอบ
    result_total = 0

    # กำหนด list ในการหาคำตอบ
    result = [[], [], []]
    
    # GOLD
    # ถ้าจำนวนสมาชิกใน list ไม่เท่า 0 และ ตัวแรกมากกว่า 0
    if len(list_a) != 0 and list_a[0] > 0:
        # นับจำนวนตัวแรก
        count_max_g = list_a.count(list_a[0])
        #ให้ตำแหน่งของจำนวนคำตอบเป็นตั้งแต่ index ที่ศูนย์ถึงตัวก่อนจำนวนที่นับของตัวแรก
        result[result_total] = (list_a[:count_max_g])
        # ให้เพิ่มจำนวนของคำตอบเท่ากับจำนวนที่นับตัวแรก
        result_total += count_max_g
    # แต่ถ้าไม่
    else:
        # ให้คืนค่า tuple ของ result
        return tuple(result)
    
    # ลบจำนวนแรกที่ใช้ไปแล้ว
    list_a = list(filter(lambda x: x is not list_a[0], list_a))
    
    # SILVER
    # ถ้าจำนวนสมาชิกใน list ไม่เท่า 0 และ จำนวนคำตอบน้อยกว่า 3
    if len(list_a) != 0 and result_total < 3:
        # ถ้าตัวแรกมากกว่า 0
        if list_a[0] > 0:
            # นับจำนวนตัวแรก
            count_max_s = list_a.count(list_a[0])
            #ให้ตำแหน่งของจำนวนคำตอบเป็นตั้งแต่ index ที่ศูนย์ถึงตัวก่อนจำนวนที่นับของตัวแรก
            result[result_total] = (list_a[:count_max_s])
            # ให้เพิ่มจำนวนของคำตอบเท่ากับจำนวนที่นับตัวแรก
            result_total += count_max_s
        # แต่ถ้าไม่    
        else:
            # ให้คืนค่า tuple ของ result
            return tuple(result)
        
    # ลบจำนวนแรกที่ใช้ไปแล้ว
    list_a = list(filter(lambda x: x is not list_a[0], list_a))

    # BRONZE
    # ถ้าจำนวนสมาชิกใน list ไม่เท่า 0 และ จำนวนคำตอบน้อยกว่า 3
    if len(list_a) != 0 and result_total < 3:
        # ถ้าตัวแรกมากกว่า 0
        if list_a[0] > 0 :
            # นับจำนวนตัวแรก
            count_max_b = list_a.count(list_a[0])
            #ให้ตำแหน่งของจำนวนคำตอบเป็นตั้งแต่ index ที่ศูนย์ถึงตัวก่อนจำนวนที่นับของตัวแรก
            result[result_total] = (list_a[:count_max_b])
        # แต่ถ้าไม่   
        else:
            # ให้คืนค่า tuple ของ result
            return tuple(result)
        
    # คืนค่า tuple ของ result
    return tuple(result)


def test():
    assert(medal_allocation([9, 8, 8, 7, 6, 5, 4, 3, 2])) == ([9], [8, 8], [])
    assert(medal_allocation([9, 8, 7, 7, 6, 5, 4, 3, 2])) == ([9], [8], [7, 7])
    assert(medal_allocation([9, 9, 8, 8, 7, 6, 5, 4, 3, 2])) == ([9, 9], [], [8, 8])
    assert(medal_allocation([9, 9, 9, 8, 7, 6, 5, 4, 3, 2])) == ([9, 9, 9], [], [])
    assert(medal_allocation([9, 9, 8, 7, 6, 5, 4, 3, 2])) == ([9, 9], [], [8])
    assert(medal_allocation([5])) == ([5], [], [])
    assert(medal_allocation([5, 7, 8, 2, 7, 1])) == ([8], [7, 7], [])
    assert(medal_allocation([9, 9, 9, 9, 9, 8, 7, 6, 5, 4, 3, 2])) == ([9, 9, 9, 9, 9], [], [])
    assert(medal_allocation([0,0,0,0,])) == ([], [], [])
    assert(medal_allocation([-4,0])) == ([], [], [])
    assert(medal_allocation([9, 9, 8, 7, 6, 5, 4, 3, 2])) == ([9, 9], [], [8])
    assert(medal_allocation([])) == ([], [], [])

    print("ALL OK")
    


    

if __name__ == '__main__' :
    main()