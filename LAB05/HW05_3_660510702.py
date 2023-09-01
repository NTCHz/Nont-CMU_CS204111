#!/usr/bin/env python3
# Thichanon Ratanasaenwan (Nont)
# 660510702
# HW05_3
# 204111 Sec 002

import string

def main():
    test_substitute_once()


# implement this function
def substitute_once(text, old, new):

    # หาตำแหน่งของคำ
    idex = text.find(old)

    # ถ้าไม่พบคำเก่าใน text ให้คืนค่าเป็น text เดิม
    if idex == -1:
        return text
    
    # คือคำที่ตั้งแต่แรกถึงคำก่อนที่เอาออกแล้วบวกคำใหม่ต่อด้วยคำตรงท้าย
    n_text = text[:idex] + new + text[idex + len(old):]

    # ส่งค่าคืน
    return n_text

# test function
def test_substitute_once():

    assert(substitute_once("battle", "b", "c")) == "cattle"
    assert(substitute_once("Bidding", "i", "u")) == "Budding"
    assert(substitute_once("doesn't", "n't", " not")) == "does not"

if __name__ == "__main__":
    main()
