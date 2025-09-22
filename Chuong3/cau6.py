def docso(n):
    hangdonvi = ["", "mot", "hai", "ba", "bon", "nam", "sau", "bay", "tam", "chin"]
    hangchuc = ["", "muoi", "hai muoi", "ba muoi", "bon muoi", "nam muoi", "sau muoi", "bay muoi", "tam muoi", "chin muoi"]
    if n < 10:
        return hangdonvi[n]
    else:
        chuc = n // 10
        donvi = n % 10
        if donvi == 0:
            return hangchuc[chuc]
        elif donvi == 5 and chuc >= 2:
            return hangchuc[chuc] + " lam"
        elif donvi == 1 and chuc >= 2:
            return hangchuc[chuc] + " mot"
        else:
            return hangchuc[chuc] + " " + hangdonvi[donvi]
for n in [5, 9, 15, 21, 36, 30, 79, 83, 95]:
    print(n, "=>", docso(n))    
    