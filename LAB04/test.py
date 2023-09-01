def is_leap_year(year):
    # ตรวจสอบว่าเป็นปีอธิกสุรทินหรือไม่
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def count_down_to_songkran(d, m, y):
    # กำหนดวันที่สงกรานต์
    songkran_day = 13
    songkran_month = 4
    
    # ตรวจสอบวันที่เริ่มต้น
    if d == songkran_day and m == songkran_month:
        return 0
    
    # นับจำนวนวันที่ห่างจากวันสงกรานต์ในปีปัจจุบัน
    if m > songkran_month or (m == songkran_month and d > songkran_day):
        next_songkran_year = y + 1
    else:
        next_songkran_year = y

    total_days = 0
    
    # นับจำนวนวันในเดือนที่มากกว่าหรือเท่ากับเดือนสงกรานต์ในปีปัจจุบัน
    if m >= songkran_month:
        total_days += (30 - d) * (13 - m)
        d = 0
    
    # นับจำนวนวันในปีปัจจุบันที่ไม่ได้เป็นเดือนสงกรานต์
    if next_songkran_year == y:
        total_days += 30 * (12 - m)
    
    # นับจำนวนวันในปีถัดไปจนถึงวันสงกรานต์
    total_days += (30 * (songkran_month - 1)) + songkran_day

    if is_leap_year(next_songkran_year):
        total_days += 1

    return total_days

d = int(input())
m = int(input())
y = int(input())

print (count_down_to_songkran(d, m, y))
