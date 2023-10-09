#!/usr/bin/env python3 
# Thichanon Ratanasaenwan (Nont)
# 660510702
# HW14_1
# 204111 Sec 002

def main():
    append_ranking()

def my_id():
    return "660510702"

def append_ranking(infile_name='score_in.txt', outfile_name='score_out.txt'):
    result = []
    list_con = []
    so = dict()
    infile = open(infile_name, 'r')
    outfile = open(outfile_name, 'a')
    for i in infile:
        total = 0
        t = i.strip()
        i = i.strip().split()
        a = i[1:]
        for _ in range(len(a)):
            if "None" in a:
                a.remove("None")
        a = list(map(float, a))
        a = sorted(a, reverse=True)
        count = 0
        for j in a:
            if count == 2:
                break

            if j == "None":
                continue

            total += float(j)
            count += 1
        
        t += " "+ str(total)
        t = t.split()
        result.append(t)

    for i in result:
        list_con.append(float(i[-1]))

    list_con = sorted(list_con, reverse=True)
    
    for i in range(len(list_con)):
        so[list_con[i]] = i+1
        
    for i in result:
        outfile.write(" ".join(i[:-1]) + " " + str(so[float(i[-1])]) + "\n")    

    infile.close()
    outfile.close()

if __name__ == '__main__':
    main()