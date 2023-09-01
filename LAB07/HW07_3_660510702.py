#!/usr/bin/env python3
# Thichanon Ratanasaenwan (Nont)
# 660510702
# HW07_3
# 204111 Sec 002

def main():
    test()

def three_digits_to_word(n):
    # สร้าง list ที่เก็บคำอ่านของตัวเลขในช่วง 0-19
    unit_list = [
        "", "one", "two", "three", "four", "five",
        "six", "seven", "eight", "nine", "ten",
        "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen"
    ]
    # สร้าง list ที่เก็บคำอ่านของตัวเลขในช่วง 20-90 (เพิ่มทีละ 10)
    tens_words = [
        '', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'
    ]

    # แยกหลัก
    hundreds, remainder = divmod(n, 100)
    tens, ones = divmod(remainder, 10)

    result = ''

    # แปลงส่วนหลักพันถ้ามีค่ามากกว่า 0
    if hundreds > 0:
        result += unit_list[hundreds] + ' hundred '

    # แปลงส่วนหลักที่เหลือถ้ามีค่ามากกว่า 0
    if remainder > 0 :
        # ถ้าค่าที่เหลือหน่อยกว่า 20
        if remainder < 20:
            # ให้เพิ่มค่าใน result ที่มาจาก unit_list
            result += unit_list[remainder] 

        # แต่ถ้าค่าที่เหลือมากกว่า 20
        else:
            # ในหลักสิบมากกว่า 0
            if tens > 0:
                # ให้เพิ่มค่าใน result ที่มาจาก tens_words
                result += tens_words[tens]
                # ในหลักหน่วยมากกว่า 0
                if ones > 0:
                    # ให้เพิ่มค่า '-' และ unit_list ของหลักหน่วยใน result 
                    result += '-' + unit_list[ones] 

            # แต่ถ้าในหลักสิบน้อยกว่า 0
            else:
                # ให้เพิ่มค่าฃอง unit_list ของหลักหน่วยใน result 
                result += unit_list[ones]

    # คืนค่า
    return result


def num_to_word(num):

    # ถ้าเลข = 0 ให้คืนค่า zero
    if num == 0 :
        return "zero"
    
    # แยกส่วนหลักพัน, หลักล้าน, หลักพัน, หลักร้อย, และหลักหน่วย
    billions, remainder = divmod(num, 1000000000)
    millions, remainder = divmod(remainder, 1000000)
    thousands, remainder = divmod(remainder, 1000)
    
    # สร้าง list result เพื่อเก็บค่า
    result = []

    # แปลงส่วนหลักพันล้านถ้ามีค่ามากกว่า 0
    if billions > 0:
        # นำค่าเข้าไปเก็บไว้ใน result
        result.append(str(three_digits_to_word(billions)))
        result.append("billion")

    # แปลงส่วนหลักล้านถ้ามีค่ามากกว่า 0
    if millions > 0:
        # นำค่าเข้าไปเก็บไว้ใน result
        result.append(str(three_digits_to_word(millions)))
        result.append("million")
    
    # แปลงส่วนหลักพันถ้ามีค่ามากกว่า 0
    if thousands > 0:
        # นำค่าเข้าไปเก็บไว้ใน result
        result.append(str(three_digits_to_word(thousands)))
        result.append("thousand")

    # แปลงส่วนหลักที่เหลือถ้ามีค่ามากกว่า 0
    if remainder > 0:
        # นำค่าเข้าไปเก็บไว้ใน result
        result.append(str(three_digits_to_word(remainder)))

    # แปลง list เป็น str แล้วคั่นด้วย " " โดยใช้ join 
    result = " ".join(result)

    # คืนค่า
    return result

def test():
    assert(num_to_word(14))  == "fourteen"
    assert(num_to_word(248))  == "two hundred forty-eight"
    assert(num_to_word(111))  == "one hundred eleven"
    assert(num_to_word(0))  == "zero"
    assert (num_to_word(42641323862)) == "forty-two billion six hundred forty-one million three hundred twenty-three thousand eight hundred sixty-two"

if __name__ == '__main__' :
    main()