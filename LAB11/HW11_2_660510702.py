#!/usr/bin/env python3
# Thichanon Ratanasaenwan (Nont)
# 660510702
# HW11_2
# 204111 Sec 002

def main():
    print(split_and_merge(3))
    # print(split_and_merge(5))

def my_id():
    return "660510702"

def arrival_sequences(left_lane, right_lane):

    # กรณีเลนซ้ายหรือเลนขวาว่าง
    if not left_lane:
        return [">".join(right_lane)]
    if not right_lane:
        return [">".join(left_lane)]
    
    # นำรถจากเลนซ้ายและเลนขวา
    from_left = left_lane[0]
    from_right = right_lane[0]

    # กรณีที่รถจากเลนซ้ายไปก่อน
    left_first = arrival_sequences(left_lane[1:], right_lane)
    left_first = list(map(lambda x: from_left + ">" + x, left_first))

    # กรณีที่รถจากเลนขวาไปก่อน
    right_first = arrival_sequences(left_lane, right_lane[1:])
    right_first = list(map(lambda x: from_right + ">" + x, right_first))

    # รวมผลลัพธ์จากทั้งสองกรณี
    return left_first + right_first

def split_and_merge(n):

    # สร้างรายการว่างเพื่อเก็บลำดับที่เป็นไปได้
    result = []

    # สร้าง list ต้นฉบับ
    original = list(map(str, range(1, n + 1)))

    # สร้างฟังก์ชันเพื่อแยกลำดับออกเป็นสองทาง
    def split(x, a, b):

        if not x:
            # เก็บค่าที่ได้จากการส่ง tuple ไปยัง func arrival_sequences
            result.extend(arrival_sequences(tuple(a),tuple(b)))
        else:
            # หาค่าแรกในลำดับ
            current = x[0]

            # เรียกตัวเองเพื่อแยกลำดับและนำไปยังสองทาง
            split(x[1:], a + [current], b)
            split(x[1:], a, b + [current])

    # เรียกใช้ฟังก์ชัน
    split(original, [], [])

    # แปลงเป็น set เพื่อเอาเลขซ้ำออก
    result = set(result)

    # เรียงลำดับ
    result = sorted(list(result))

    # คืนค่า
    return result

if __name__ == '__main__':
    main()