var2 = (10,20,"Hello",True,(333,"WoW"),"oo")

varTemp = list(var2)
varTemp[2] = "Hi"
var2 = tuple(varTemp)
print(var2)