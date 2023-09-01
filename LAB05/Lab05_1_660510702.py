#!/usr/bin/env python3
# Thichanon Ratanasaenwan (Nont)
# 660510702
# Lab05_1
# 204111 Sec 002

def main():
    test_minute_diff()


# implement this function
def minute_diff(hour1, min1, period1, hour2, min2, period2):

    #ฟังก์ชั่นแปลงจาก AM PM เป็น 24 ชั่วโมง
    def changhour(hour, period):
        if period == 'AM':
            if hour == 12:
                return 0
            else:
                return hour
        else:
            if hour == 12:
                return 12
            else:
                return hour + 12
    
    # เรียกใช้ฟังก์ชั่น changhour
    hour1 = changhour(hour1, period1)
    hour2 = changhour(hour2, period2)

    #ผลรวมนาทีของแต่ละเวลา
    sum1 = hour1 * 60 + min1
    sum2 = hour2 * 60 + min2

    # หาโดยการเอานาทีทั้งหมดของอันแรกลบอันที่สอง แล้วใส่ abs
    return abs(sum1 - sum2)


# test function
def test_minute_diff():
    assert(minute_diff(8, 23, "AM", 8, 24, "AM")) == 1
    assert(minute_diff(8, 23, "AM", 1, 24, "PM")) == 301
    assert(minute_diff(1, 24, "PM", 8, 23, "AM")) == 301

if __name__ == "__main__":
    main()
