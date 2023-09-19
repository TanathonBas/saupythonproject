def inputPH():
    province = input("จังหวัด:")
    ph = int(input("ค่า PH: "))
    return province, ph

def checkph(ph):
    if ph == 7 or  ph == 8:
        return 'Result is Normal'
    elif ph > 8:
        return 'Result is Acid'
    else:
        return 'Result is Alkali'
    
def showph(province, ph):
    print(f'จังหวัด : {province} ค่า PH : {ph}')

province, ph = inputPH()
showph(province,checkph(ph))
