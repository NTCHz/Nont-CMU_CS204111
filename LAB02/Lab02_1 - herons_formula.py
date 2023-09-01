#!/usr/bin/env python3
# Thichanon Ratanasaenwan (Nont)
# 660510702
# Lab02_1
# 204111 Sec 002

import math #import module math

a = float(input("a: ")) #input a
b = float(input("b: ")) #input b
c = float(input("c: ")) #input c

s = (a+b+c)/2 #find s

A = math.sqrt(s*(s-a)*(s-b)*(s-c)) #find area and sqrt

print("area: ",math.ceil(A)) #print A use math.ceilS