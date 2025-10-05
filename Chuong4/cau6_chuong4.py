from random import randrange
print("Ví dụ 10 giá trị ngẫu nhiên trong khoảng 1-100")
for i in range(10):
    print(randrange(1,100),end='\t')

print("\nCác giá trị có thể xuất hiện là các số nguyên từ 0 đến 99")
print("Các giá trị sau KHÔNG thể xuất hiện: 4.5, -1, 100")
print("Các giá trị sau có thể xuất hiện: 0, 35, 99")