#!/usr/bin/env python3 
# Thichanon Ratanasaenwan (Nont)
# 660510702
# Lab12_1
# 204111 Sec 002

import math

def my_id():
    return "660510702"

def main():
    while True:
        x = int(input())
        y = int(input())
        display_calendar(x, y)
    pass

def display_calendar(month, year):

    month_true = month
    year_true = year

    # ปรับค่าเดือนและปีเพื่อให้เข้ากับ Gregorian Calendar
    if month < 3:
        month += 12
        year -= 1
    
    # คำนวณวันของสัปดาห์โดยใช้ Gregorian Calendar
    k = year % 100
    j = year // 100

    day_of_week = (1 + 13*(month + 1)//5 + k + k//4 + j//4 - 2*j) % 7
    
    if day_of_week == 0:
        day_of_week = 7
        
    # หาจำนวนวันในเดือน
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (year_true % 4 == 0 and year_true % 100 != 0) or (year_true % 400 == 0):
        days_in_month[1] = 29

    print("Su Mo Tu We Th Fr Sa")

    print("-- "*(day_of_week - 1), end="")

    for i in range(1, days_in_month[month_true - 1]+1):   
        print(f"{i:2} ", end="")
        day_of_week += 1
        if day_of_week == 8:
            print()
            day_of_week = 1

    print("\n")

if __name__ == "__main__":
    main()