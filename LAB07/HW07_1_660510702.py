#!/usr/bin/env python3
# Thichanon Ratanasaenwan (Nont)
# 660510702
# HW07_1
# 204111 Sec 002

def main():
    test()

def print_polynomial(pc_list, v):
    
    # เรียง list ที่มี tuple เป้ฯสมาชิก โดยใช้ sorted ตำแหน่งที่ x[] แล้วกลับด้าน
    pc_list_sorted = sorted(pc_list, key=lambda x: x[0], reverse=True)

    # ฟังก์ชั่นแปลง ในแต่ละ tuple ใน list
    def format_pc(power, coefficient):

        # ถ้าตัวจำนวนเต็มเป็น 0 ให้ return ""
        if coefficient == 0:
            return ""
        # ถ้า absolute จำนวนเต็มเป็น 1 และ เลขชี้กำลังเท่ากับ 0 ให้ return ""
        if abs(coefficient) == 1 and power > 0:
            coefficient_str = "" 
        # แต่ถ้าไม่ให้ return str absolute จำนวนเต็ม
        else :
            coefficient_str = str(abs(coefficient))
        # ถ้า ตัวชี้กำลัง มากกว่า 0
        if power > 0:
            # ถ้าเป็นเลข 1 ให้ return โดยไม่ต้องใส่เลขชี้กำลัง
            if power == 1:
                # เช็คว่าจำนวนเต็มน้อยกว่า 0 หรือไม่ให้ใส่เครื่องหมายข้างหน้า
                return f"{'-' if coefficient < 0 else '+'} {coefficient_str}{v}"
            # แต่ถ้าไม่ให้ return โดยมีเลขชี้กำลัง
            else:
                # เช็คว่าจำนวนเต็มน้อยกว่า 0 หรือไม่ให้ใส่เครื่องหมายข้างหน้า
                return f"{'-' if coefficient < 0 else '+'} {coefficient_str}{v}^{power}"
        # ถ้าตัวชี้กำลังน้อยกว่าหรือเท่ากับ 0 ให้ return จำนวนเต็มเดิม
        else:
            # เช็คว่าจำนวนเต็มน้อยกว่า 0 หรือไม่ให้ใส่เครื่องหมายข้างหน้า
            return f"{'-' if coefficient < 0 else '+'} {coefficient_str}"
        
    # เรียกใช้ func format_pc โดยใช้ list, map, lambda โดยการแยกทีละ tuple แล้วแยกตัวใน tuple ส่งค่าเข้าไปใน func 
    pc_list_str = list(map(lambda x: format_pc(x[0], x[1]) , pc_list_sorted))

    # ทำเป็น str โดยใช้ join ที่มีช่องว่างคั่น
    pc_list_str = ' '.join(pc_list_str)

    # ลบช่องว่างที่ตัวแรก
    pc_list_str = pc_list_str.replace(" ","",1)

    # ถ้าตัวแรกมีเครื่องหมายเป็น + ให้ลบบวกตัวแรกแแกโดยใช้ slice
    if pc_list_str[0] == '+':
        pc_list_str = pc_list_str[1:]

    # คืนค่า
    return (pc_list_str)

def test():
    print (print_polynomial([(2, -6), (3, 5), (1,34)], 'x'))
    print (print_polynomial([(2, -6), (1, 0), (3,34)], 'y')) 

if __name__ == '__main__' :
    main()