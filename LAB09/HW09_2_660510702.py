#!/usr/bin/env python3
# Thichanon Ratanasaenwan (Nont)
# 660510702
# HW09_2
# 204111 Sec 002

def my_id():
    return "660510702"

def main():
    test()

def median_of_median(list_a):
    
    '''
    หาโดยการหาความยาวแล้วหาร 3 ไม่เอาเศษเเพื่อที่จะตัด list_a เป็นสามส่วน
    จากนั้นก็เรียกใช้ฟังก์ชั่นเดิมโดยที่หา median ของแต่ละอันไปเรื่อยๆแล้วนำกลับมารวมกันทำซ้ำ
    จนเหลือเพียงตัวเดียวแล้วให้คืนค่าตัวนั้นเป็นค่า float
    '''

    
    if len(list_a) == 0:
        return []

    if len(list_a) == 1:
        return list_a[0]
    
    if len(list_a) == 2:
        return (list_a[0] + list_a[1]) / 2
    
    if len(list_a) == 3:
        Max_ = max(list_a)
        Min_ = min(list_a)
        return sum(list_a) - Max_ - Min_
            
    len_list = len(list_a)
    len_li = len_list // 3
    list_A = median_of_median(list_a[:len_li])
    list_B = median_of_median(list_a[len_li:len_li*2])
    list_C = median_of_median(list_a[len_li*2:])
    list_a = [list_A, list_B, list_C]
    return float(median_of_median(list_a))
    
def test():
    print (median_of_median([2, 3, 2, 1, 1, 1, 1]))
    print (median_of_median([28, 14, 13, 21, 19, 27, 23, 30, 16, 3]))

    # 1111223
if __name__ == '__main__':
    main()