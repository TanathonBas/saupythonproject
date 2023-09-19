def calculatetourcost(numpeople):
    if 1 <= numpeople <= 2:
        packagecost = 300
    elif 3 <= numpeople <= 5:
        packagecost = 250
    elif 6 <= numpeople <= 10:
        packagecost = 210
    else:
        packagecost = 150
    
    totalcost = numpeople * packagecost
    averagecost = totalcost / numpeople
    return totalcost, averagecost

def main():
    groupleadername = input("ป้อนชื่อหัวหน้ากรุ๊ปทัวร์: ")
    contactnumber = input("ป้อนเบอร์โทรศัพท์ติดต่อกลับ: ")
    
    try:
        numpeople = int(input("ป้อนจำนวนคนที่จะไปทัวร์: "))
        if numpeople < 1:
            print("โปรดป้อนจำนวนคนที่ถูกต้อง.")
            return
    except ValueError:
        print("โปรดป้อนจำนวนคนที่ถูกต้อง.")
        return
    
    total_cost, average_cost = calculatetourcost(numpeople)
    
    print("\nข้อมูลการท่องเที่ยว")
    print("ชื่อหัวหน้ากรุ๊ปทัวร์:", groupleadername)
    print("เบอร์โทรศัพท์ติดต่อกลับ:", contactnumber)
    print("จำนวนคนที่จะไปทัวร์:", numpeople)
    print("ค่าใช้จ่ายทั้งหมด: {} บาท".format(total_cost))
    print("ค่าเฉลี่ยต่อคน: {} บาท".format(average_cost))

if __name__ == "__main__":
    main()
