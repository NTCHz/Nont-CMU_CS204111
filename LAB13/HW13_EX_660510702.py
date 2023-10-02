#!/usr/bin/env python3 
# Thichanon Ratanasaenwan (Nont)
# 660510702
# HW13_EX
# 204111 Sec 002

def my_id():
    return "660510702"

def main():
    print(sand_towers([4, 8]))
    # print(sand_towers([4, 4, 4]))
    # print(sand_towers([9, 12, 6]))

def sand_towers(size_tower):
    # var
    text = ""

    # list block tower
    list_tower = ["|>>~","|"]
    list_body_top = ["/^^^\\","/     \\","/^^^^^^^\\"]

    count = 0

    max_size_tower = max(size_tower)
    result = [[] for _ in range(max_size_tower+2)]

    for i in range(len(size_tower)):
        # ปัจจุบัน
        current = []

        # แถวแรกที่เป็นจุดยอด กรณีที่เป็นตัวแรก
        if size_tower[i] == max_size_tower and count == 0:
            current.append(" "*(size_tower[i] + 1) + list_tower[0] + " "*(size_tower[i]-4))
            current.append(" "*(size_tower[i] + 1) + list_tower[1] + " "*(size_tower[i]-1))

            for body_top in range(1,4):
                current.append(" "*(size_tower[i] - body_top) + list_body_top[body_top-1] + " "*(size_tower[i]-body_top -2))

            for j in range(size_tower[i]-4):
                if j == size_tower[i]-5:
                    current.append(" "*(size_tower[i]- (j+4)) + "/" + " "*((j+5)*2-1) + "\\")
                    continue
                current.append(" "*(size_tower[i]- (j+4)) + "/" + " "*((j+5)*2-1) + "\\" + " "*(size_tower[i] - (j+4)-2))
            
            for k in range(1,max_size_tower+2):
                result[k] += current[k-1]

            count = 1

        # แถวแรกที่เป็นจุดยอด กรณีที่เป็นตัวต่อไป
        elif size_tower[i] == max_size_tower and count > 0:
            current.append(" "*(size_tower[i] + 1) + list_tower[0] + " "*(size_tower[i] - 4))
            current.append(" "*(size_tower[i] + 1) + list_tower[1] + " "*(size_tower[i] - 1))

            for body_top in range(1,4):
                if body_top == 3 and size_tower[i] == 4:
                    current.append(list_body_top[body_top-1])
                    continue
                current.append(" "*(size_tower[i] - body_top) + list_body_top[body_top-1] + " "*(size_tower[i]-body_top-2))

            for j in range(size_tower[i]-4):
                if j == size_tower[i]-5:
                    current.append("/" + " "*((j+5)*2-1) + "\\")
                    continue
                current.append(" "*(size_tower[i]- (j+4)) + "/" + " "*((j+5)*2-1) + "\\" + " "*(size_tower[i] - (j+4)-2))

            for k in range(1,max_size_tower+2):
                result[k] += current[k-1]

        # แถวต่อไปที่ไม่เป็นจุดยอด กรณีที่เป็นตัวแรก
        elif size_tower[i] != max_size_tower and count == 0:
            for _ in range(max_size_tower+2 - (size_tower[i] - 1)):
                current.append(" "*(size_tower[i]*2+1))

            for body_top in range(1,4):
                current.append(" "*(size_tower[i] - body_top) + list_body_top[body_top-1] + " "*(size_tower[i]-body_top -2))

            for j in range(size_tower[i]-4):
                if j == size_tower[i]-5:
                    current.append(" "*(size_tower[i]- (j+4)) + "/" + " "*((j+5)*2-1) + "\\")
                    continue
                current.append(" "*(size_tower[i]- (j+4)) + "/" + " "*((j+5)*2-1) + "\\" + " "*(size_tower[i] - (j+4)-2))
            
            for k in range(1,max_size_tower+2):
                result[k] += current[k]
            count = 1

        # แถวต่อไปที่ไม่เป็นจุดยอด กรณีที่เป็นตัวต่อไป
        elif size_tower[i] != max_size_tower and count > 0:
            for _ in range(max_size_tower+2 - (size_tower[i] - 1)):
                current.append(" "*(size_tower[i]*2+1))

            for body_top in range(1,4):
                if body_top == 3 and size_tower[i] == 4:
                    current.append(list_body_top[body_top-1])
                    continue
                current.append(" "*(size_tower[i] - body_top) + list_body_top[body_top-1] + " "*(size_tower[i]-body_top-2))

            for j in range(size_tower[i]-4):
                if j == size_tower[i]-5:
                    current.append("/" + " "*((j+5)*2-1) + "\\")
                    continue
                current.append(" "*(size_tower[i]- (j+4)) + "/" + " "*((j+5)*2-1) + "\\" + " "*(size_tower[i] - (j+4)-2))

            for k in range(1,max_size_tower+2):
                result[k] += current[k]
            
            
    # join result 
    for i in result:
        text += "".join(i)
        text += "\n"

    # บรรทัดสุดท้าย
    for i in size_tower:
        text += "/"
        text += ":"*(i*2)
    text += ":\\"

    return text


if __name__=="__main__":
    main()