#!/usr/bin/env python3
# Thichanon Ratanasaenwan (Nont)
# 660510702
# HW11_3
# 204111 Sec 002

def main():
    runner_up()

def my_id():
    return "660510702"

def runner_up():
    
    in_ = int(input("Total students: "))    
    
    max_score = -1  
    runner_up_ = -1  
    total_score = 0 
    i = 0
    print("Enter score: ")

    while i < in_:
        in_x = float(input())
        total_score += in_x

        if in_x < max_score and in_x > runner_up_ and max_score != -1:
            runner_up_ = in_x

        if in_x > max_score:
            runner_up_ = max_score
            max_score = in_x

        i += 1
        

    Average = total_score / in_
    print("---")
    print("Max score is: {:.2f}".format(max_score))
          
    if runner_up_ < 0 :
        print("Runner up is: {}".format(None))
    else:
        print("Runner up is: {:.2f}".format(runner_up_))
        
    print("Average is: {:.2f}".format(Average))


        
if __name__ == '__main__':
    main()