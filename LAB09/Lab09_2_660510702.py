#!/usr/bin/env python3
# Thichanon Ratanasaenwan (Nont)
# 660510702
# Lab09_2
# 204111 Sec 002

def my_id():
    return "660510702"

def main():
    test()

def life_path(n):
    # แปลง int เป็น list โดยแปลงเป็น str ก่อน จะสามารถแยกหลักออกจากกันได้
    list_n = list(str(n))

    # base
    if len(list_n) == 1:
        return int("".join(list_n))
    
    # แปลงสมาชิกใน list เป็น int
    list_n = list(map(int,list_n))

    # คืนค่าผลรวมของตัวเลข
    return life_path(sum(list_n))

def test():
    print(life_path(13092004))
    print(life_path(7))
    print(life_path(35))
    
if __name__ == '__main__':
    main()