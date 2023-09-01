#!/usr/bin/env python3
# Thichanon Ratanasaenwan (Nont)
# 660510702
# Lab02_2
# 204111 Sec 002

milli = int(input("Input millisecounds: ")) #input millisecounds

sec = milli // 1000 #find Secound left
milli %= 1000  #find milli

minute = sec // 60 #find minute left
sec %= 60 #find Secound 

hour = minute // 60 #find hour left
minute %= 60 #find minute 

Day = hour // 24 #find Day
hour %= 24 #find hour

print("{} day(s), {} hour(s), {} minute(s), {} secound(s), and {} millisec(s)".format(Day, hour, minute, sec, milli)) #print Date