def inputemployee():
    idemployee = int(input("รหัสพนักงาน:"))
    nameemployee = input("ชื่อพนักงาน:")
    moneyemployee = float(input("ยอดขายที่ทำได้:"))
    return idemployee, nameemployee, moneyemployee

def checkemployee(moneyemployee):
    if moneyemployee >= 1001 or moneyemployee == 2000:
        return moneyemployee * (1 / 100)
    elif moneyemployee >= 2001 or moneyemployee == 3000:
        return moneyemployee * (3 / 100)
    elif moneyemployee >= 3000:
        return moneyemployee * (5 / 100)
    else:
        return moneyemployee * 0
    
def showemployee(idemployee, nameemployee, commission):
    print(f"รหัสพนักงาน : {idemployee} ชื่อพนักงาน : {nameemployee} ค่าคอม : {commission:.2f}")

idemployee, nameemployee, moneyemployee = inputemployee()
commission = checkemployee(moneyemployee)
showemployee(idemployee, nameemployee, commission)