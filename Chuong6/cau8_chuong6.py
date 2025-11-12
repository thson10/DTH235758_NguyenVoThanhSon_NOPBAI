n = int(input("Nhập số phần tử: "))
lst = [float(input(f"Nhập số thứ {i+1}: ")) for i in range(n)]

lst.sort(reverse=True)
print("Dãy giảm dần:", lst)