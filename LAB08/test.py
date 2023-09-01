# def calculate_term(k):
#     if k % 2 == 0:
#         return 4 / (k * (k + 1) * (k + 2))
#     else:
#         return -4 / (k * (k + 1) * (k + 2))

# def pi(n):
#     if n == 0:
#         return 3
#     else:
#         return pi(n-1) + calculate_term(2*n)

# # ตัวอย่างการเรียกใช้งานฟังก์ชัน
# print("pi(0) =", pi(0))  # ผลลัพธ์ที่ควรได้: 3
# print("pi(2) =", pi(2))  # ผลลัพธ์ที่ควรได้: 3.133333
# print("pi(5) =", pi(5))  # ผลลัพธ์ที่ควรได้: 3.142713
def base_b(x ,b):
    if x == 0:
        return x
    elif x%b == 0:
        return '0'
    return base_b((x*10) // b, b)+ str(x // b)