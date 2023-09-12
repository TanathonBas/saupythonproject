def inputcardetail():
    carNo = input("ป้อนทะเบียนรถ")
    carWeight = float(input("ป้อนน้ำหนักรถ"))
    return carNo, carWeight

def checkcalAndShowweight(carNo,carWeight):
    if carWeight > 1000 :
        print(f"{carNo} น้ำหนักรถไม่ผ่านเกณฑ์")
    else :
        print(f"{carNo} น้ำหนักรถผ่านเกณฑ์")

print("--------------------------")
print("truck Checker")
print("--------------------------")
carNo, carWeight = inputcardetail()
print("--------------------------")
checkcalAndShowweight(carNo, carWeight)
print("--------------------------")