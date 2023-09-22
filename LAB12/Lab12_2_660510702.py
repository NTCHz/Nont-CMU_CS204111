#!/usr/bin/env python3 
# Thichanon Ratanasaenwan (Nont)
# 660510702
# Lab12_2
# 204111 Sec 002

def my_id():
    return "660510702"

def main():
    print(multiply_polynomials([2,0,3],[4,5]))

def multiply_polynomials(p1,p2):

    # คำนวณความยาวของผลคูณ
    result_length = len(p1) + len(p2) - 1

    result = [0] * result_length  

    # คูณโพลินอมิแอล p1 กับ p2 และรวมผลลัพธ์
    for i in range(len(p1)):
        for j in range(len(p2)):
            result[i + j] += p1[i] * p2[j]

    return result

if __name__ == '__main__':
    main()