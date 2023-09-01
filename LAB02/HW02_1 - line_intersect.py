#!/usr/bin/env python3
# Thichanon Ratanasaenwan (Nont)
# 660510702
# HW02_1
# 204111 Sec 002

m1 = float(input("m1: ")) #input m1
b1 = float(input("b1: ")) #input b1
m2 = float(input("m2: ")) #input m2
b2 = float(input("b2: ")) #input b2

# y1 = m1x + b1 , y2 = m2x + b2 #mathematical equations

x = (b2 - b1) / (m1 - m2) #find x

y = m1 * x + b1 #find y

print("Line intersect at ({:.2f},{:.2f})".format(x,y)) #print Line intersect (x,y)