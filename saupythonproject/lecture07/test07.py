#การเข้าถึงข้อมูลทุกข้อมูลใน list และ tuple
var1 = [10,20,"Hello",True,[333,"WoW"],"oo"]

var2 = (10,20,"Hello",True,(333,"WoW"),"oo")

for data in var1:
    print(data)
    
for data in var2:
    print(data)