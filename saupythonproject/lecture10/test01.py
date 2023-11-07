try :
    num1 = int( input ("Input number 1 : "))
    num2 = int( input ("Input number 2 : "))

    result1 = num1 * num2
    result2 = num1 / num2

    print(f'{num1} X {num2} = {result1}')
    print(f'{num1} X {num2} = {result2}') 
except ValueError :
    print("ตรวจสอบการป้อนข้อมูล เนื่องจากป้อนข้อมูลไม่ถูกต้อง")
except ZeroDivisionError :
    print("ตรวจสอบการป้อนข้อมูล ตัวเลขตัวที่ 2 ต้องห้ามเป็น 0")
except Exception :
    print("มีข้อผิดพลาดเกิดขึ้น กรุณาติดต่อฝ่ายบริการ")
finally :
    print("WoW wow wow")
