#!/usr/bin/env python3
# Thichanon Ratanasaenwan (Nont)
# 660510702
# HW02_3
# 204111 Sec 002

Old_P = float(input("Old Price: ")) #input Old_Price

x = (((Old_P-50)//100) *100) + 98 # find New_P โดยนำ Old_P ไปลบ 50 หาร 100 ไม่เอาเศษ จะได้หลักร้อยมา แล้วนำไปคูณ 100 บวก 98

print ("New Price: ",int(x)) #print New_Price  