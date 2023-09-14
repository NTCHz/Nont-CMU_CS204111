#!/usr/bin/env python3
# Thichanon Ratanasaenwan (Nont)
# 660510702
# HW11_1
# 204111 Sec 002

import string

def main():
    # assert words_to_num("fourteen") == 14
    print(words_to_num("two hundred forty-eight"))
    print(words_to_num("forty-two billion six hundred forty-one million three hundred twenty-three thousand eight hundred sixty-two"))
    # print(words_to_num("one hundred eleven"))
    # assert words_to_num("forty-two billion six hundred forty-one million three hundred twenty-three thousand eight hundred sixty-two") == 42641323862

def my_id():
    return "660510702"

def words_to_num(words):
    words = words.lower().replace("-"," ").split()
    total = 0
    cur_num = 0

    digit = {
        "zero" : 0, 
        "one" : 1, "two" : 2, "three" : 3, "four" : 4, "five" : 5,
        "six" : 6, "seven" : 7, "eight" : 8, "nine" : 9, "ten" : 10, 
        "eleven" : 11, "twelve" : 12, "thirteen" : 13, "fourteen" : 14, "fifteen" : 15, 
        "sixteen" : 16, "seventeen" : 17, "eighteen" : 18, "nineteen" : 19, "twenty" : 20, 
        "thirty" : 30, "forty" : 40, "fifty" : 50, "sixty" : 60, 
        "seventy" : 70, "eighty" : 80, "ninety" : 90, "hundred" : 100,  
        "thousand" : 1000, "million" : 1000000, "billion" : 1000000000
    }
    for word in words:
        if word in digit:
            num = digit[word]
            if num == 100:  # กรณีคำว่า "hundred"
                cur_num *= num

            elif num == 1000 or num == 1000000 or num == 1000000000:  # กรณีคำว่า "thousand" หรือ "million" หรือ "billion"
                total += cur_num * num
                cur_num = 0
                
            else:
                cur_num += num
                
    total += cur_num
    return total


if __name__=='__main__':
    main()