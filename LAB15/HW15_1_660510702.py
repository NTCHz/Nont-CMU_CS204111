#!/usr/bin/env python3 
# Thichanon Ratanasaenwan (Nont)
# 660510702
# HW15_1
# 204111 Sec 002

def main():
    shelf = [('Bleach', 10), ('Naruto', 5), ('One Piece', 24)] 
    new = ('Naruto', 18) 
    manga_add(shelf, new, True) 
    print('--') 
    print(shelf)

    shelf = [('Bleach', 100), ('Bleach', 10000)] 
    new = ('Bleach', 99) 
    manga_add(shelf, new) 
    print('--') 
    print(shelf)

def my_id():
    return "660510702"

def manga_add(manga_shelf, new_m, show_steps=False):

    left = 0 
    right = len(manga_shelf) - 1

    while left <= right:
        mid = (left + right) // 2

        if show_steps:
            print(f'[{mid}] {manga_shelf[mid]}')
        
        if manga_shelf[mid] < new_m:
            left = mid + 1
        else:
            right = mid - 1

    manga_shelf.insert(left, new_m)

if __name__ == '__main__':
    main()

