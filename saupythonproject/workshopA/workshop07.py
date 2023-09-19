def inputnumUser():
    numscore = int(input("กรอกตัวเลข: "))
    return numscore

def checknumUser(numscore):
    if numscore == 25 :
        print("Correct, You are the winner")
    else:
        print("Not Correct !!!.")

def showAnswer(answer):
    return answer

numscore = inputnumUser()
answer = checknumUser(numscore)
showAnswer(answer)