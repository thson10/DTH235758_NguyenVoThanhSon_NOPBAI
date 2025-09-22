import datetime

def NgayKeTiep(ngay, thang, nam):
    try:
        date = datetime.date(nam, thang, ngay)
        next_day = date + datetime.timedelta(days=1)
        return next_day.day, next_day.month, next_day.year
    except ValueError:
        return "Ngay khong hop le"
def namnhuan(nam):
    if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
        return True
    else:
        return False          
#main
ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))
if thang in [1,3,5,7,8,10,12]:
    if ngay < 1 or ngay > 31:
        print("Ngày không hợp lệ")
        exit()
elif thang in [4,6,9,11]:
    if ngay < 1 or ngay > 30:
        print("Ngày không hợp lệ")
        exit()
elif thang == 2:
    if ngay < 1 or ngay > 29:
        print("Ngày không hợp lệ")
        exit()
else: 
    d,m,y = NgayKeTiep(ngay,thang,nam)
    print(f"Ngày kế tiếp là: {d},{m},{y}")
    exit()
"""import datetime

def NgayKeTiep(ngay, thang, nam):
    try:
        date = datetime.date(nam, thang, ngay)
        next_day = date + datetime.timedelta(days=1)
        return next_day.day, next_day.month, next_day.year
    except ValueError:
        return "Ngay khong hop le"
    
#main
ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))
d,m,y = NgayKeTiep(ngay,thang,nam)
print(f"Ngày kế tiếp là: {d}/{m}/{y}")"""