#!/usr/bin/env python3 
# Thichanon Ratanasaenwan (Nont)
# 660510702
# HW13_2
# 204111 Sec 002

def main():
    print (count_vote([['Mewtwo', 'Pikachu', 'Suicune'], 
 ['Mewtwo', 'Suicune', 'Pikachu'], 
 ['Pikachu', 'Rayquaza', 'Charizard'], 
 ['Suicune', 'Pikachu', 'Charizard']]))

def my_id():
    return '660510702'

def count_vote(pref_matrix):

    scores_p = {}

    for i in pref_matrix:
        # หาคะแนนสูงสุด
        voters = len(i)
        for j in i:
            if j in scores_p:
                scores_p[j] += voters
                voters -=1
            else:
                scores_p[j] = voters
                voters -=1


    # แปลงดิกชันนารีเป็นรายการ tuple และ sorted
    sorted_scores = sorted(scores_p.items(), key=lambda x: (-x[1], x[0]))
    
    return sorted_scores


if __name__ == '__main__':
    main()