#!/usr/bin/env python3
# Thichanon Ratanasaenwan (Nont)
# 660510702
# Lab07_1
# 204111 Sec 002

def main():
    test()

def corner_frame(n):

    # หาออกมาโดยการใช้ list, map และ range โยการใช้ join สร้าง str โดยการเทียบเลขโดยใช้ range 
    # EX. อย่างแรกใช้ map ในการใช้ range ตั้งแต่ 1 ถึง n+1 เพราะ range จะให้ค่าตั้งแต่ตัวเริ่มต้นแล้วไปถึงตัวก่อนตัวสุดท้ายเลย + 1
    #     เพื่อส่ง argument ไปเป็น parameter ใน lambda โดยตั้งชื่อ parameter เป็น i
    #     นั้นก็ใช้ join เพื่อเชื่อมข้อมูล โดยเว้นวรรค (' ') ทุกตัว โดยการใช้ map และ lambda เหมือนตัวแรก
    #     แต่จะเป็นการเทียบค่าระหว่าง parameter i (ตอนแรก) กับ parameter j โดยที่ถ้ามากกว่าหรือเท่ากับ i ให้ค่า string
    #     ที่มี index เป็น j แต่ถ้าไม่ใช้ จะให้ค่า string ที่มี index เป็น i 
    result = list(map(lambda i: ' '.join(map(lambda j: str(j) if j >= i else str(i) ,range(1,n+1))),range(1,n+1)))
    # ใช้ '\n' ในการเชื่อม string ของแต่ละแถว
    return "\n".join(result) + "\n"
    

def test():
    # print(corner_frame(4))
    print(corner_frame(2))

if __name__ == '__main__' :
    main()