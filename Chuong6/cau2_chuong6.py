from random import randrange

lst = []
n = int(input("Nhập số phần tử: "))
for i in range(n):
    lst.append(randrange(0, 100))

print("List ngẫu nhiên:", lst)
x = int(input("Mời bạn chèn thêm số mới: "))
lst.append(x)
print("List sau khi chèn:", lst)

k = int(input("Nhập số để xóa: "))
while k in lst:
    lst.remove(k)
print("List sau khi xóa:", lst)

def CheckDoiXung(lst):
    for i in range(len(lst)):
        if lst[i] != lst[len(lst)-i-1]:
            return False
    return True

if CheckDoiXung(lst):
    print("List đối xứng")
else:
    print("List không đối xứng")