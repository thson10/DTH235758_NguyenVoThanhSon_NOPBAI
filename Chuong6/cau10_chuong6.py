m = int(input("Nhập số dòng: "))
n = int(input("Nhập số cột: "))

print("Nhập ma trận A:")
A = [[float(input(f"A[{i}][{j}]=")) for j in range(n)] for i in range(m)]
print("Nhập ma trận B:")
B = [[float(input(f"B[{i}][{j}]=")) for j in range(n)] for i in range(m)]
# Cộng ma trận
C = [[A[i][j] + B[i][j] for j in range(n)] for i in range(m)]
print("Ma trận A+B:\n", C)

# Hoán vị (transpose)
AT = [[A[i][j] for i in range(m)] for j in range(n)]
BT = [[B[i][j] for i in range(m)] for j in range(n)]
print("Hoán vị A:\n", AT)
print("Hoán vị B:\n", BT)