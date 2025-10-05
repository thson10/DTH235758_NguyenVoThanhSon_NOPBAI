from math import sqrt

print("Chương trình diện tích tam giác")
a = float(input("Nhập độ dài cạnh a: "))
b = float(input("Nhập độ dài cạnh b: "))
c = float(input("Nhập độ dài cạnh c: "))
if(a <= 0 or b  <= 0 or c <= 0 or (a + b <= c) or (a + c <= b) or (b + c <= a)):
    print("Tam giác không hợp lệ")
else:
    cv = a + b + c
    p = cv / 2
    dt = sqrt(p * (p - a) * (p - b) * (p - c))
    print("Diện tích = ",dt)    