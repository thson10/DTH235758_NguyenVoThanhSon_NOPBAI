from random import randrange

def TaoMaTran(m, n):
    return [[randrange(100) for _ in range(n)] for _ in range(m)]

def XuatMaTran(D):
    for row in D:
        print('\t'.join(map(str, row)))

def LayDong(D, r):
    return D[r]

def LayCot(D, c):
    return [D[i][c] for i in range(len(D))]

def TimMax(D):
    return max(max(row) for row in D)

m = int(input("Nhập số dòng: "))
n = int(input("Nhập số cột: "))
D = TaoMaTran(m, n)
XuatMaTran(D)

r = int(input("Nhập dòng muốn xuất: "))
print("Dòng", r, ":", LayDong(D, r))

c = int(input("Nhập cột muốn xuất: "))
print("Cột", c, ":", LayCot(D, c))

print("Số lớn nhất trong ma trận =", TimMax(D))