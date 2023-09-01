import string
A = 'HGFHSA'
A = list(A)

# def Check_H(X) :
#     if X in string.digits:
#         return True
    
# B = list(filter(Check_H, A))
# if len(A) == len(B):
#     print("ตัวใหญ่ทั้งหมด")
# else:
#     print("ผสม")

if A[0] in string.ascii_uppercase:
    print (True)