#!/usr/bin/env python3
# Thichanon Ratanasaenwan (Nont)
# 660510702
# Lab05_2
# 204111 Sec 002

def main():
    test_zodiac_element()


# implement this function
def zodiac_element(year):

    #ฟังก์ชั่นคำนวณพลังหยินหยาง
    def yin_yang(year):
        if year % 2 == 1:
            return "Yin"
        else:
            return "Yang"
        
    #ฟังก์ชั่นคำนวณปีนักษัตรจีน
    def Chinese_zodiac_year(year):
        year = year % 12   
        if year == 0:
            return "Monkey"
        elif year == 1:
            return "Rooster"
        elif year == 2:
            return "Dog"
        elif year == 3:
            return "Pig"
        elif year == 4:
            return "Rat"
        elif year == 5:
            return "Ox"
        elif year == 6:
            return "Tiger"
        elif year == 7:
            return "Rabbit"
        elif year == 8:
            return "Dragon"
        elif year == 9:
            return "Snake"
        elif year == 10:
            return "Horse"
        elif year == 11:
            return "Goat"
    
    #ฟังก์ชั่นคำนวณธาตุประจำปี
    def yearly_elements(year):
        year //= 2
        year %= 5
        if year == 0:
            return "Metal"
        elif year == 1:
            return "Water"
        elif year == 2:
            return "Wood"
        elif year == 3:
            return "Fire"
        elif year == 4:
            return "Earth"
    
    #ส่งค่าคืน
    return ("{} {} {}".format(yin_yang(year), yearly_elements(year), Chinese_zodiac_year(year)))



# test function
def test_zodiac_element():

    assert(zodiac_element(1997)) == "Yin Fire Ox"
    assert(zodiac_element(2022)) == "Yang Water Tiger"


if __name__ == "__main__":
    main()
