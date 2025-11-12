lst = []
n = int(input("Nhập số phần tử: "))

for i in range(n):
    while True:
        val = float(input(f"Nhập phần tử thứ {i+1}: "))
        if i == 0 or val > lst[-1]:
            lst.append(val)
            break
        else:
            print("Giá trị không tăng, nhập lại!")
print("Dãy tăng dần:", lst)