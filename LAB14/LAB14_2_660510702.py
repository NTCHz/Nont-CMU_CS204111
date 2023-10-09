#!/usr/bin/env python3 
# Thichanon Ratanasaenwan (Nont)
# 660510702
# LAB14_2
# 204111 Sec 002

def main():
    list_x = [('11/Jan/1900', 'Event A'), ('5/Dec/2001', 'Event B'), 
          ('5/Dec/2002', 'Event C'), ('21/Aug/2008', 'Event D'), 
          ('9/Mar/2013', 'Event E'), ('11/Mar/2017', 'Event F'), 
          ('7/May/2019', 'Event G'), ('29/Feb/2032', 'Event H'), 
          ('9/Nov/2042', 'Event I')] 
    event = search_event(list_x, '29/Feb/2032', show_steps=True) 
    print('---') 
    print(event) 

    list_x = [('11/Jan/1900', 'Event A'), ('5/Dec/2001', 'Event B'), 
          ('5/Dec/2002', 'Event C'), ('21/Aug/2008', 'Event D'), 
          ('9/Mar/2013', 'Event E'), ('11/Mar/2017', 'Event F'), 
          ('7/May/2019', 'Event G'), ('29/Feb/2032', 'Event H'), 
          ('9/Nov/2042', 'Event I')] 
    event = search_event(list_x, '23/Aug/2008', show_steps=True) 
    print('---') 
    print(event) 
 


def my_id():
    return "660510702"

def less_than(date1, date2):
    date2 = str(date2)
    months = {
        'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4,
        'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8,
        'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12
    }

    day1, month1, year1 = date1.split('/')
    day2, month2, year2 = date2.split('/')

    year1, year2 = int(year1), int(year2)
    month1, month2 = months[month1], months[month2]
    day1, day2 = int(day1), int(day2)

    if year1 < year2:
        return "<"
    elif year1 > year2:
        return ">"
    else:
        if month1 < month2:
            return "<"
        elif month1 > month2:
            return ">"
        else:
            if day1 < day2:
                return "<"
            elif day1 > day2:
                return ">"

def search_event(list_x, key, show_steps=False):
    lo = 0
    hi = len(list_x) -1

    while lo <= hi:
        mid = (lo + hi) // 2
        if show_steps:
                print(f"[{mid}]: {list_x[mid][0]}")
        if key == list_x[mid][0]:
            return list_x[mid]
        else:
            if less_than(key ,list_x[mid][0]) == "<":
                hi = mid - 1
            else:
                lo = mid + 1
    

if __name__ == "__main__":
    main()