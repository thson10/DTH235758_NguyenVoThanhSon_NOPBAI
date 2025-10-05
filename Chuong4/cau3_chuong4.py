def BMI(height, weight):
    return weight / (height ** 2)
def PhanLoai(bmi):
    if bmi < 18.5:
        return "Gầy"
    elif bmi <= 24.9:
        return "Bình thường"
    elif bmi <= 29.9:
        return "Hơi béo"
    elif bmi <= 34.9:
        return "Béo phì cấp độ 1"
    elif bmi <= 39.9:
        return "Béo phì cấp độ 2"
    else: 
        return "Béo phì cấp độ 3"
def NguyCoBenh(bmi):
    if bmi < 18.5:
        return "Nguy cơ bệnh thấp"
    elif bmi <= 24.9:
        return "Nguy cơ bệnh trung bình"
    elif bmi <= 29.9:
        return "Nguy cơ bệnh cao"
    elif bmi <= 34.9:
        return "Nguy cơ bệnh cao"
    elif bmi <= 39.9:
        return "Nguy cơ bệnh rất cao"
    else: 
        return "Nguy cơ bệnh cực kỳ nguy hiểm"
print("Chương trình tính chỉ số BMI")
print("Nhập vào chiều cao (m): ")
height = float(input())
print("Nhập vào cân nặng (kg): ")
weight = float(input())
bmi = BMI(height, weight)
print("Chỉ số BMI = ",bmi) 
print("Phân loại: ", PhanLoai(bmi))
print("Nguy cơ bệnh: ", NguyCoBenh(bmi))