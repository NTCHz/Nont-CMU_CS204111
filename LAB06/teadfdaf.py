
def main():
    decode("aceiklmr-", '''
3 .
5 3 4 2 .
3 1 2 8 1 7 2 0 86 .
''')

def decode(code_table, text):

    text = text.replace(".", "")
    lis = text.split("\n")

    def Xhaa(x):
        str_index = list(map(int, (lis[x].split())))
        print(decode_helper(code_table, str_index))

    list(map(Xhaa ,range(1, len(lis) - 1)))
            
def decode_helper(code_table, str_index):
    ans = "".join(map(lambda j: code_table[j] if j < len(code_table) and j > -(len(code_table)) else '_', str_index))
    return ans

if __name__ == '__main__':
    main()
