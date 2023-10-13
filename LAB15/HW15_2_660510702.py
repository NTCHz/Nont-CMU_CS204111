#!/usr/bin/env python3 
# Thichanon Ratanasaenwan (Nont)
# 660510702
# HW15_2
# 204111 Sec 002

import math

def main():
    histpram((19, 39, 59, 42, 42, 42, 100))

def my_id():
    return "660510702"

def histpram(scores):
    list_original = ["_____","*****","|"]
    list_r = [0] * 10
    high_list = [0] * 10
    for i in scores:
        if i >= 0 and i <= 10:
            list_r[0] += 1
        elif i >= 11 and i <= 20:
            list_r[1] += 1
        elif i >= 21 and i <= 30:
            list_r[2] += 1
        elif i >= 31 and i <= 40:
            list_r[3] += 1
        elif i >= 41 and i <= 50:
            list_r[4] += 1
        elif i >= 51 and i <= 60:
            list_r[5] += 1
        elif i >= 61 and i <= 70:
            list_r[6] += 1
        elif i >= 71 and i <= 80:
            list_r[7] += 1
        elif i >= 81 and i <= 90:
            list_r[8] += 1
        elif i >= 91 and i <= 100:
            list_r[9] += 1

    for i in range (len(list_r)):
        high_list[i] = (math.ceil(list_r[i] / 5))

    print(high_list)
    hightest = max(high_list)
    print(high_list)
    maxhigh = hightest + 2
    print(maxhigh)
    list_result = []
    for i in range (len(high_list)):
        space = 2
        if i > 9:
            space = 1
        listcur = []
        if high_list[i] == hightest:
            listcur.append(" "*space + str(list_r[i]) + "\n" + list_original[0] + "\n" + ((list_original[1] + "\n")*high_list[i]))
        else:
            listcur.append(((" " * 5 + "\n")*(hightest-high_list[i]-1))+"\n" + " "*space + str(list_r[i]) + "\n"+ list_original[0] + "\n" + (((list_original[1] + "\n")*high_list[i])*high_list[i]))        
        list_result.append(listcur)
    
    for i in range(maxhigh):
        for j in range(len(list_result)):
            print("".join(list_result[j]), end="")

    print("0" + " "*5 + "10" + " "*4 + "20" + " "*4 + "30" + " "*4 + "40" + " "*4 + "50" + " "*4 + "60" + " "*4 + "70" + " "*4 + "80" + " "*4 + "90" + " "*4 + "100")
if __name__ == '__main__':
    main()