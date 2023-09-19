def calculatenetsalary(salary):
    tax = salary * 7 / 100
    socialsecurity = 500
    netsalary = salary - tax - socialsecurity
    return netsalary

def getemployeeinfo():
    employeeID = input("ป้อนรหัสพนักงาน:")
    employeeName = input("ป้อนชื่อพนักงาน:")
    salary = float(input("ป้อนเงินเดือนปกติของพนักงาน:"))
    return employeeID, employeeName, salary

def result(employeeID,employeeName,salary,netsalary):
    print(f"รหัสพนักงาน {employeeID}")
    print(f"ชื่อพนักงาน {employeeName}")
    print(f"เงินเดือนปกติ {salary:.2f}บาท")
    print(f"เงินเดือนสุทธิ {netsalary:.2f}บาท")

employeeID, employeeName, salary = getemployeeinfo()
netsalary = calculatenetsalary(salary)
result(employeeID,employeeName,salary,netsalary)
