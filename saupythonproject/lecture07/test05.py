#list/tuple function
var1 = [10,20,"Hello",True,[333,"WoW"],"oo"]

var2 = (10,20,"Hello",True,(333,"WoW"),"oo")

print(f'ใน var1 มีข้อมูลทั้งหมด {len(var1)} ข้อมูล')
print(f'ใน var2 มีข้อมูลทั้งหมด {len(var2)} ข้อมูล')
#min/max ใช้ไม่ได้กับข้อมูลคนฃะชนิดกัน
var3 = [10,20,30,True,10,20]
var4 = (10,20,30,True,10,20)
print(min(var3))
print(max(var4))