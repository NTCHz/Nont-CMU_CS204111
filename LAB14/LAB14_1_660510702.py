#!/usr/bin/env python3 
# Thichanon Ratanasaenwan (Nont)
# 660510702
# LAB14_1
# 204111 Sec 002

def main():
    list_x = ['11/ม.ค./2643', '5/ธ.ค./2542', '19/ม.ค./2546', '11/ก.ย./2544'] 
    sort_date(list_x, show_steps=True) 
    print('---') 
    print(list_x)

    list_x = ['11/ม.ค./2643', '5/ธ.ค./2542', '19/ม.ค./2546', '11/ก.ย./2544'] 
    sort_date(list_x) 
    print('---') 
    print(list_x)

def my_id():
    return "660510702"

def less_than(date1, date2):

        months = {
            'ม.ค.': 1, 'ก.พ.': 2, 'มี.ค.': 3, 'เม.ย.': 4,
            'พ.ค.': 5, 'มิ.ย.': 6, 'ก.ค.': 7, 'ส.ค.': 8,
            'ก.ย.': 9, 'ต.ค.': 10, 'พ.ย.': 11, 'ธ.ค.': 12
        }

        day1, month1, year1 = date1.split('/')
        day2, month2, year2 = date2.split('/')

        year1, year2 = int(year1), int(year2)
        month1, month2 = months[month1], months[month2]
        day1, day2 = int(day1), int(day2)

        if year1 < year2:
            return True
        elif year1 == year2 and month1 < month2:
            return True
        elif year1 == year2 and month1 == month2 and day1 < day2:
            return True
        else:
            return False
        
def sort_date(list_x, show_steps=False):
    n = len(list_x)
    for i in range(1, n):
        j = i 
        while j > 0 and less_than(list_x[j], list_x[j-1]):
                list_x[j], list_x[j-1] = list_x[j-1], list_x[j]
                j -= 1

        if show_steps:
            print(f"{i}: {list_x}") 

if __name__ == "__main__":
    main()