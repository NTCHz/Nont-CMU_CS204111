#!/usr/bin/env python3
# Thichanon Ratanasaenwan (Nont)
# 660510702
# HW10_2
# 204111 Sec 002

import string

def my_id():
    return "660510702"

def main():
    print(unmask_id('1-2345-67890-**-*'))
    print(unmask_id('1-2345-67890-12-*'))
    # print(unmask_id('1-2345-67**0-12-1'))

def unmask_id(masked_id):
    r = []
    c = 13
    a = 0
    id = masked_id.replace("-","")
    if len(id) != 13:
        return False
    
    if id[12] == "*":
        id_ = id
        for i in range(0,10):
            id_ = list(id)
            if id.count("*") >= 2:
                idx = id.index("*")
                id_[idx] = i

            while c > 0 :
               
                for i in id_:
                    if i != "*":
                        a += int(i)*c
                    c -= 1 

            c = 13
            a = a % 11 
            b = 11 - a
            d = b % 10
            a = 0

            idx = id_.index("*")
            id_[idx] = d

            result = list(map(str, id_))
            result = [result[0] + "-" + "".join(result[1:5]) + "-" + "".join(result[5:10]) + "-" + "".join(result[10:12]) + "-" + result[-1]]
            r += result
    else:
        for i in range (0,10):
            for j in range(0,10):
                id_ = list(id)
                if id.count("*") >= 2:
                    idx = id.index("*")
                    id_[idx] = i
                    id_[idx+1] = j

                while c > 0 :
                    for i in id_[:-1]:
                        a += int(i)*c
                        c -= 1 

                c = 13
                a = a % 11 
                b = 11 - a
                d = b % 10
                if str(d) == id[12]:
                    result = list(map(str, id_))
                    result = [result[0] + "-" + "".join(result[1:5]) + "-" + "".join(result[5:10]) + "-" + "".join(result[10:12]) + "-" + result[-1]]
                    r += result

                a = 0

    if id.count("*") == 1:
        return [r[0]]
    
    return(r) 

if __name__ == '__main__':
    main()