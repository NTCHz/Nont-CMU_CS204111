#!/usr/bin/env python3
# Thichanon Ratanasaenwan (Nont)
# 660510702
# Lab06_1
# 204111 Sec 002

def main():
    for i in range(3, 20):
        print(triangle(i))


def triangle(n):
    
    def check(x):
        if x == 1:
            return ('*')
        else:
            return ('*' + '.'*(2 * x - 3) + '*')
        
    l_n = list(range(1, int(abs(n))))
    a = list(map(check,l_n))
    a.append('* '*n)
    result = '\n'.join(a)
    return result + '\n'


# def test_triangle():

#     T3 = '''*
# *.*
# * * *
# '''

#     T7 = '''*
# *.*
# *...*
# *.....*
# *.......*
# *.........*
# * * * * * * *
# '''

#     # assert triangle(3) == T3
#     # assert triangle(7) == T7
#     # print(triangle(8))
#     # triangle(7)
#     # print("OK")

#     while True :
#         X = int(input())
#         print(triangle(X))


if __name__ == '__main__':
    main()
