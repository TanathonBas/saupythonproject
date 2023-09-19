def calculate_average(score01,score02,score03):
    totol_score = score01 + score02 + score03
    average_score = totol_score / 3
    return average_score

def inputstudeninfo():
    studen_ID = input("ป้อนรหัสนักเรียน: ")
    studen_NAME = input("ป้อนชื่อนักเรียน: ")
    return studen_ID, studen_NAME

def getScores():
    score01 = float(input("ป้อนคะแนนครั้งที่ 1 : "))
    score02 = float(input("ป้อนคะแนนครั้งที่ 2 : "))
    score03 = float(input("ป้อนคะแนนครั้งที่ 3 : "))
    return score01, score02, score03

studen_ID, studen_NAME = inputstudeninfo()
score01, score02, score03 = getScores()
average = calculate_average(score01, score02, score03)

def showresult():
    print(f"รหัสนักเรียน: {studen_ID}")
    print(f"ชื่อนักเรียน: {studen_NAME}")
    print(f"คะแนนนักเรียน: {average:.2f}")

showresult()