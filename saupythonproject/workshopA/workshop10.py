def inputstudentYear():
    return int(input('ปีการศึกษา : '))
    

def checkstudentYear(studentYear):
    if studentYear == 66:
        return 'Welcome Freshman'
    elif studentYear == 65:
        return 'Welcome Sophomore'
    elif studentYear == 64:
        return 'Welcome Junior'

def showstudentYear(year,studentYear):
    print(f'ปีการศึกษา : {year} : {studentYear}')

studentYear = inputstudentYear()
checkYear = checkstudentYear(studentYear)
showstudentYear(studentYear,checkYear)