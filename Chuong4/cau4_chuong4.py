def ROI(dt,cp):
    return (dt-cp)/cp
def GOIYDAUTU(roi):
    if(roi >= 0.75):
        return "Nên đầu tư"
    else:
        return "Không nên đầu tư"
print("Chương trình tính ROI")
dt = float(input("Nhập doanh thu (Triệu VND): "))
cp = float(input("Nhập chi phí (Triệu VND): "))
roi = ROI(dt, cp)
print("Chỉ số ROI = ",roi)
print("===>", GOIYDAUTU(roi))