#!/usr/bin/env python3
# Thichanon Ratanasaenwan (Nont)
# 660510702
# HW04_2
# 204111 Sec 002

def main():
    # รับค่า
    d = int(input())
    m = int(input())
    y = int(input())
    
    # แสดงผล
    print (count_down_to_songkran(d, m, y))

# ฟังก์ชั่นในการหาวัน
def count_down_to_songkran(d,m,y):

    #กำหนดปีเพื่อคำนวนวันในเดือน feb
    if m > 4 or (m == 4 and d > 13):
        y += 1
    else :
        y

    # กำหนดวันในเดือน feb
    if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0):
        feb = 29
        
    else:
        feb = 28
    
    #กำหนดวันในแต่ละเดือน
    jan = 31
    mar = 31
    apr = 30
    may = 31
    jun = 30
    jul = 31
    aug = 31
    sep = 30
    oct_= 31
    nov = 30
    dec = 31
    
    #เงื่อนไขในแต่ละเดือน
    #ถ้าเป็นในเดือน n จะบวกเดือนต่อไปแล้วบวกวันที่ 13 ในวันสงกรานต์ แล้วลบวันที่ input ออก
    if m == 1: 
        return jan  + feb + mar + 13 - d 
    elif m == 2: 
        return feb + mar + 13 - d 
    elif m == 3:
        return mar + 13 - d
    elif m == 4:
        if d > 13 :
            return mar + may + jun + jul + aug + sep + oct_ + nov + dec + jan + feb + mar + 13 - d - 1 # ลบ 1 เพราะลบวันของมันเองอีกที
        elif d < 13 :
            return 13 - d
        else :
            return 0
    elif m == 5:
        return may + jun + jul + aug + sep + oct_ + nov + dec + jan + feb + mar + 13 - d
    elif m == 6:
        return jun + jul + aug + sep + oct_ + nov + dec + jan + feb + mar + 13 - d
    elif m == 7:
        return jul + aug + sep + oct_ + nov + dec + jan + feb + mar + 13 - d
    elif m == 8:
        return aug + sep + oct_ + nov + dec + jan + feb + mar + 13 - d
    elif m == 9:
        return sep + oct_ + nov + dec + jan + feb + mar + 13 - d
    elif m == 10:
        return oct_ + nov + dec + jan + feb + mar + 13 - d
    elif m == 11:
        return nov + dec + jan + feb + mar + 13 - d
    elif m == 12:
        return dec + jan + feb + mar + 13 - d

if __name__ == '__main__':
    main()