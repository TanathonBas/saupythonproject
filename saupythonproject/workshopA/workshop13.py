def inputstudentinfo():
    studentID = input("รหัสนักเรียน:")
    studentNAME = input("ชื่อรักเรียน:")
    studentGrade = float(input("เกรดเฉลี่ยนักเรียน:"))
    return studentID, studentNAME, studentGrade

def checkstudentGrade(studentID, studentNAME, studentGrade):
    if studentGrade >= 2.00:
        return f'รหัสนักเรียน {studentID} ชื่อนักเรียน {studentNAME} ได้เกรดเฉลี่ย {studentGrade} สอบผ่าน'
    else:
        return f'รหัสนักเรียน {studentID} ชื่อนักเรียน {studentNAME} ได้เกรดเฉลี่ย {studentGrade} สอบไม่ผ่าน'
    
def main():
    numstudent = int(input("ป้อนจำนวนนักเรียนที่ต้องการตรวจสอบ:"))
    
    for i in range(numstudent):
        studentID, studentNAME, studentGrade = inputstudentinfo()
        result = checkstudentGrade(studentID, studentNAME, studentGrade)
        print(result)

main()