import math

def canbac2(n):
    result = 0
    for i in range(n):
        result += math.sqrt(2 + result)
    return result
n = int(input("Nhập n: "))
ketqua = canbac2(n)
print(f"Kết quả sau {n} lần lồng căn bậc 2 là: {ketqua}")
