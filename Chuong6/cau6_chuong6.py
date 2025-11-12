from random import sample

n = int(input("Nhập số phần tử: "))
lst = sample(range(0, 1000), n)
print("List ngẫu nhiên không trùng:", lst)