from math import log
print("Chương trình tính logarit")
print("Nhập vào x (x > 0): ")
x = float(input())
print("Nhập vào a (a > 0): ")
a = float(input())
if x > 0 and a > 0 and a != 1:
    loga_x = log(x) / log(a)   
    print(f"log_a({x}) = {loga_x}")