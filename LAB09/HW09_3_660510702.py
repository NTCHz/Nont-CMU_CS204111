#!/usr/bin/env python3
# Thichanon Ratanasaenwan (Nont)
# 660510702
# HW09_3
# 204111 Sec 002

def my_id():
    return "660510702"

def main():
    test()

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

def test():
    print (arrival_sequences(('R32',), ('O9', 'O5')))
    print (arrival_sequences(('R2', 'R4'), ('O34', 'O22')))

if __name__ == '__main__':
    main()