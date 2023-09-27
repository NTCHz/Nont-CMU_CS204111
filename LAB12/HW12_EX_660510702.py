#!/usr/bin/env python3 
# Thichanon Ratanasaenwan (Nont)
# 660510702
# HW12_EX
# 204111 Sec 002

def my_id():
    return "660510702"

def main():
    while True:
        x = int(input())
        print(xmas_tree(x)) 

def xmas_tree(n):
    
    tree = "\n"
    if n < 1:
        return ""
    
    # ส่วนบน
    tree += (" "*(n+4)) + ("|\n")
    tree += (" "*(n+2)) + ("--*--\n")
    tree += (" "*(n+3)) + ("/|\\\n")
    tree += (" "*(n+2)) + ("/* *\\\n")

    # ส่วนกลาง 3 แถว
    for i in range(n):
        for a in range(3):
            tree += " "*(2-a)
            for _ in range(n-i-1):
                tree += (" ")

            tree += ("/")
            for _ in range(a+2+i):
                tree += ("* ")
            
            tree += ("*\\\n")

    # ส่วนล่าง
    tree += (" ")*(n+3) + ("|||\n")
    tree += ("_")*(n+3) + ("|||") + ("_")*(n+3) + ("\n")

    # คืนค่า
    return tree    
    

if __name__ == "__main__":
    main()