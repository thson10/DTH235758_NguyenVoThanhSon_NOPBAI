from random import randrange
while True:
    somay = randrange(1, 101)
    solandoan = 0
    win = False
    while solandoan < 7:
        solandoan += 1
        songuoi = int(input("Máy đoán (1-100), mời bạn đoán: "))
        print("Bạn đoán lần thứ ", solandoan)
        if somay == songuoi:
            print("Chúc mừng bạn đã đoán đúng, số máy là: ", somay)
            win = True
            break
        if somay < songuoi:
            print("Số máy nhỏ hơn số bạn đoán")
        elif somay > songuoi:
            print("Số máy lớn hơn số bạn đoán")   
    if win == False:
        print("GAME OVER!, số máy là: ", somay)      
    hoi = input("Bạn có muốn chơi tiếp không (c/k): ")
    if (hoi == 'k'):
        break   
print("Cảm ơn bạn đã chơi Game!")        
