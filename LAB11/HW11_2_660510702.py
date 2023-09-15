#!/usr/bin/env python3
# Thichanon Ratanasaenwan (Nont)
# 660510702
# HW11_2
# 204111 Sec 002

def main():
    print(split_and_merge(3))
    # print(split_and_merge(4))

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
    a = list(map(str ,range(1,n+1)))
    a = "".join(a)
    list_result = []
    
    for i in range(n):
        left = tuple((a[0]))
        right = tuple((a[1:]))
        list_result += arrival_sequences(left,right)
        a = a[1:] + a[0]

    list_result = set(list_result)
    result = list(list_result)
    return result
        


    


if __name__ == '__main__':
    main()