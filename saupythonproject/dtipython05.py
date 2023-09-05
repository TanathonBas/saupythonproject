#คำนวณเงินที่จะแชร์กัน ป้อนเงิน ป้อนคน แล้วคำนวณและแสดงเงินที่จะแชร์กันทางหน้าจอ
#โดยให้เขียนฟังก์ชัน ขอ 2 ฟังก์ชัน

#รับข้อมูล
def inputmoneyPerson( ):
    money=float(input('ป้อนจำนวนเงิน:'))
    person=int(input('ป้อนจำนวนคน:'))
    return money, person
    
#คำนวณ
def calAndShowMoneyShare(money,person ):
    doublefloatmoney="%.2f"% money
    print(f'จำนวณเงิน {money:} บาท คน {person} แชร์กันคนละ {round(float(money/person))} บาท')
    print('จำนวณเงิน' ,doublefloatmoney, 'บาท' ,person, 'คน แชร์กันคนละ' ,(round(money/person)), 'บาท')#ใช้ ,
    print('จำนวนเงิน' +str("%.2f"%money)+ 'บาท' +str(person)+ 'คน แชร์กันคนละ' +str(round(money/person))+ 'บาท' )#ใช้ +
    print('จำนวนเงิน {:.2f} บาท {} คน แชร์กันคนละ {} บาท'.format (money), (person), {round(money/person)})#ใช้เมธอต format
    print('จำนวนเงิน %s บาท %d คน แชร์กันคนละ %d บาท'%(doublefloatmoney,person,round(money/person)))#ใฃ้ %

money,person=inputmoneyPerson()

calAndShowMoneyShare(money,person )