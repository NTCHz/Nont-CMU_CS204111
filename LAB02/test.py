import random

A = []
S = [30]
i = 1

while( i <= 5 ):
    r = random.randint(1, 25)
    if( r not in A ):
        A.append( r )
        i = i + 1

A.sort()
print(A)
# for i in range (5):
#     r = random.randint(1, 25)
#     A.append(r)

User = float(input())
for j in range (5):
    if (abs(User - A[j])) < (abs(S[0] - User)):
        S[0] = A[j] 
    elif (abs(User - A[j])) == (abs(S[0] - User)):
        S.append(A[j])

S.sort()
print(S[0])
