#!/usr/bin/env python3
# Thichanon Ratanasaenwan (Nont)
# 660510702
# Lab09_1
# 204111 Sec 002

def my_id():
    return "660510702"

def main():
    test()

def patterned_message(message, pattern):
    # แทนที่ช่องว่าง
    message = message.replace(" ","")

    # เช็คว่า message พอต่อ pattern หรือไม่
    def check_message(message, pattern):
        if len(message) >= len(pattern):
            return message
        
        if len(message) < len(pattern):
            return check_message(message * 2, pattern)
        
    # เรียกใช้ func check_message
    message = check_message(message, pattern)

    # base
    if len(pattern) == 0:
        return
    
    # ถ้า pattern ตัวแรก เป็น * ให้ print ตัวแรก แล้วเรียกใช้ฟังก์ชั่น patterned_message โดยที่ลบตัวแรกของทั้งสองออก
    if pattern[0] == "*":
        print(message[0],end="")
        patterned_message(message[1:], pattern[1:])

    # ถ้า pattern ตัวแรก เป็น " " ให้ print " " แล้วเรียกใช้ฟังก์ชั่น patterned_message โดยที่ลบตัวแรกของ pattern ออก
    elif pattern[0] == " ":
        print(" ",end="")
        patterned_message(message, pattern[1:])

    # ถ้า pattern ตัวแรก เป็น "\n" ให้ print "\n" แล้วเรียกใช้ฟังก์ชั่น patterned_message โดยที่ลบตัวแรกของ pattern ออก
    elif pattern[0] == "\n":
        print("\n",end="")
        patterned_message(message, pattern[1:])

def test():
    patterned_message("123", "** *** ** ** *")
    patterned_message("D and C",''' 
*************** 
******   ****** 
*************** 
''')
    patterned_message("Three Diamonds!",''' 
    *     *     * 
   ***   ***   *** 
  ***** ***** ***** 
   ***   ***   *** 
    *     *     * 
''')
    
if __name__ == '__main__':
    main()