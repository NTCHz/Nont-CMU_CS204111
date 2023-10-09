#!/usr/bin/env python3
# ชื่อ ธนารักษ์ กันยาประสิทธิ์ คิว
# 660510655
# HW13_EX
# 204111 Sec 002

def main():
    list_x = ['11/ม.ค./2643', '5/ธ.ค./2542', '19/ม.ค./2546', '11/ก.ย./2544']
    # list_x = ['11/ม.ค./2643', '5/ธ.ค./2542', '19/ม.ค./2546', '11/ก.ย./2544']
    sort_date(list_x, show_steps=True)
    print('---')
    print(list_x)

def sort_date(list_x, show_steps=False):
    show_steps_list = []

    for i in range(len(list_x)):
        list_x[i] = list_x[i].split("/")

    #!-----------------------------------------------------------------------------------

    
    count = 1
    for i in range(1, len(list_x)):
        months = {
            'ม.ค.': 1, 'ก.พ.': 2, 'มี.ค.': 3, 'เม.ย.': 4,
            'พ.ค.': 5, 'มิ.ย.': 6, 'ก.ค.': 7, 'ส.ค.': 8,
            'ก.ย.': 9, 'ต.ค.': 10, 'พ.ย.': 11, 'ธ.ค.': 12
        }
        j = i
        while j > 0:
            # Compare years
            if int(list_x[j][2]) < int(list_x[j - 1][2]):
                list_x[j], list_x[j - 1] = list_x[j - 1], list_x[j]

            # Compare months
            elif int(list_x[j][2]) == int(list_x[j - 1][2]) and months[list_x[j][1]] < months[list_x[j - 1][1]]:
                list_x[j], list_x[j - 1] = list_x[j - 1], list_x[j]

            # Compare days
            elif int(list_x[j][2]) == int(list_x[j - 1][2]) and months[list_x[j][1]] == months[list_x[j - 1][1]] and \
                    int(list_x[j][0]) < int(list_x[j - 1][0]):
                list_x[j], list_x[j - 1] = list_x[j - 1], list_x[j]

            else:
                break

            j -= 1

        if show_steps:
            a = list(map(lambda x: "/".join(x) , list_x))
            print(f'{count}: {a}')
        
        count += 1
        

    #!-----------------------------------------------------------------------------------
    
    for i in range(len(list_x)):
        list_x[i] = "/".join(list_x[i])

if __name__ == "__main__":
    main()
