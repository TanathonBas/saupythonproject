def calculateinterest(loanamount):
    if loanamount >= 1000:
        interestrate = 2.5
    else:
        interestrate = 5.5
    return interestrate

def result(borrower_name, loan_amount, interest_rate):
    print(f"ผู้กู้: {borrower_name}")
    print(f"จำนวนเงินกู้: {loan_amount} บาท")
    print(f"อัตราดอกเบี้ย: {interest_rate} %")

def main():
    borrower_name = input("ชื่อผู้กู้: ")
    loan_amount = float(input("จำนวนเงินกู้ (บาท): "))

    interest_rate = calculateinterest(loan_amount)
    result(borrower_name, loan_amount, interest_rate)

main()
