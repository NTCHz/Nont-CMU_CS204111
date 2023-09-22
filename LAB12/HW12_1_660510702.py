#!/usr/bin/env python3 
# Thichanon Ratanasaenwan (Nont)
# 660510702
# HW12_1
# 204111 Sec 002

def my_id():
    return "660510702"

def main():
    print(scramble('Cat'))
    print(scramble('bee'))
    print(scramble('bEe'))

def scramble(word):

    def permutations(current, remaining):
        if not remaining:
            possible_words.add(current)
            return

        for i in range(len(remaining)):
            new_current = current + remaining[i]
            new_remaining = remaining[:i] + remaining[i + 1:]
            permutations(new_current, new_remaining)

    # ตรวจสอบว่า input ประกอบด้วยตัวอักษรภาษาอังกฤษเท่านั้น
    if not word.isalpha() or not word.isascii():
        return []

    # สร้างเซตเพื่อเก็บคำที่เป็นไปได้ทั้งหมด
    possible_words = set()

    # สร้าง permutations
    permutations('', word)

    return list(possible_words)

if __name__ == '__main__':
    main()