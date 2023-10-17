class DtiSau :
    stu_name = ''
    score = 0
    gpa = 0

    def histudent(self):
        print(f'สวัสดี {self.stu_name}')

    def showScoreAndGpa(self):
        print(f'คะแนน {self.score} ได้GPA {self.gpa}')

obj01 = DtiSau()
obj02 = DtiSau()

obj01.stu_name = 'สมชาย'
obj01.histudent()
obj01.stu_name = 'สมหญิง'
obj02.score = 99
obj02.gpa = 3.00
obj02.showScoreAndGpa()