f_dti = open("myfile01.txt", "r" , encoding="utf-8")

try :
    data = f_dti.read()

    for data_by_line in data:
        print(data_by_line,end='')
except Exception:
    print("ติดต่อ admin")
finally:
    f_dti.close()