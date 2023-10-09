#!/usr/bin/env python3 
# Thichanon Ratanasaenwan (Nont)
# 660510702
# HW14_2
# 204111 Sec 002

def main():
    test_bottom_up_m_sort_first()
    test_bottom_up_m_sort_sec()
    test_bottom_up_m_sort_thrid()

def my_id():
    return "660510702"

def bottom_up_m_sort(list_x, show_steps=False):
    
    # first
    for i in range(len(list_x)):
        list_x[i] = [list_x[i]]
    if show_steps:
        print(list_x)

    # func recursive
    def help(list_x, show_steps):
        if len(list_x) == 1:
            return
        
        list_copy = list_x[:]
        list_x.clear()
        # merge
        for i in range(0,len(list_copy),2):
            re = []
            fe = []
            re.append(list_copy[i:i+2])
            for j in range(len(re)):
                for k in re[j]:
                    fe += k

                # sort
                n = len(fe)
                for i in range(n):
                    for j in range(0, n-i-1):
                        if fe[j] > fe[j+1]:
                            fe[j], fe[j+1] = fe[j+1], fe[j]
                
                list_x.append(fe)

        if show_steps:
            print(list_x)

        # recursive
        help(list_x, show_steps)

    # recursive    
    help(list_x, show_steps)
    
    list_x[:] = list_x[0]

def test_bottom_up_m_sort_first():
    list_x = [64, 34, 25, 12, 22, 11, 90, 100, 1, 50, 20, 11,50,60]
    bottom_up_m_sort(list_x, True) 
    print('--------') 
    print(list_x)

def test_bottom_up_m_sort_sec():
    list_x = [3, 7, 4, 9, 5, 2, 6, 1]
    bottom_up_m_sort(list_x) 
    print('--------') 
    print(list_x)

def test_bottom_up_m_sort_thrid():
    list_x = list_x = [3, 7, 4, 9, 5, 2, 6] 
    bottom_up_m_sort(list_x, True) 
    print('--------') 
    print(list_x) 

if __name__ == "__main__":
    main()
