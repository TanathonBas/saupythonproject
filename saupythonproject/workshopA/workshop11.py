def inputTelephon():
    user = input("ชื่อผู้ใช้:")
    tel = int(input("เบอร์ผู้ใช้:"))
    timeMinuet = int(input("จำนวนนาที:"))
    return user, tel, timeMinuet

def checkTelephonebill(timeMinuet):
    if timeMinuet == 1 & timeMinuet <= 15:
        return timeMinuet
    elif timeMinuet == 16 & timeMinuet <= 30:
        return timeMinuet * 3
    else:
        return timeMinuet * 1.5
    
def showTelephone(user, tel, timeMinuet, service):
    print(f"ชื่อผู้ใช้: {user} เบอร์ : {tel} จำนวนนาที : {timeMinuet} ค่าบริการ : {service}")

user, tel, timeMinuet = inputTelephon()
service = checkTelephonebill(timeMinuet)
showTelephone(user, tel, timeMinuet, service)