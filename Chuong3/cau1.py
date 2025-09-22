print("Chuong trinh kiem tra nam nhuan")
year = int(input("Nhap vao nam: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Nam", year, "la nam nhuan")
else:
    print("Nam", year, "khong phai la nam nhuan")    