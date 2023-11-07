f_dti = open("myfile01.txt", "r" , encoding="utf-8")

try :
    data = f_dti.readline()
    print(data)
    data = f_dti.readline()
    print(data)
except Exception:
    print("ติดต่อ admin")
finally:
    f_dti.close()