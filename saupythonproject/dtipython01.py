#function 1 : No paramiter No return
def funcA( ) :
    print("AAA")
    #ไม่ควรเรียกfunctionไปมา
    print("BBB")
    #ไม่มีคำสั่ง return
    
def funcB( ):
    print(111)

funcA( )
funcA( )
funcB( )
funcA( )
