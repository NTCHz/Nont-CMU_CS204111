#!/usr/bin/env python3
# Thichanon Ratanasaenwan (Nont)
# 660510702
# Lab07_2
# 204111 Sec 002

import string

def main():
    test()

def square_frame(n, sep=' '):
    
    #หาตัวเลขทั้งหมดโดยใช้ list, map, range
    range_n = list(map(str,range(1,n**2-((n-2)**2)+1)))

    # หาหลักที่มากที่สุดของตัวเลข
    max_digit = len(str(n**2-((n-2)**2)))

    #เติมหลักให้เท่ากัน
    fill = list(map(lambda x : x.zfill(max_digit),range_n))

    # แยกจำนวนใน list ขวา
    mid1 = fill[n:n+n-2]
    # กลับด้าน list ซ้าย
    mid2 = fill[::-1]
    # แยกจำนวนใน list ซ้าย
    mid2 = mid2[0:n-2]
    
    # หาเลขในบรรทัดตรงกลาง
    mid = list(map(lambda x: mid2[x] + sep*((len(fill[:n])-2) * max_digit) +sep*(n-1) + mid1[x],range(0,n-2)))
    # แปลงจำนวนตรงกลางจาก list เป็น str แล้วเว้นบรรทัด
    mid = "\n".join(mid)

    # หาเลขในบรรทัดแรก
    first = sep.join(fill[:n])

    # หาเลขบรรทัดสุดท้าย
    end = fill[-(n+(n-2)):-(n-2)]

    # กลับด้าน
    end.reverse()
    # แปลงบรรทัดสุดท้ายจาก list เป็น str
    end = sep.join(end)
    
    # แสดงค่า
    print (first + "\n" + mid + "\n" + end)
    

def test():
    square_frame(3)
    square_frame(4, '.')

if __name__ == '__main__' :
    main()