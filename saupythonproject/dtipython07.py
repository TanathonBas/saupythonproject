#โปรแกรมคำนวนหาพื้นที่วงกลม เส้นรอบวง และปริมาตรทรงกลม จากรัศมีที่ป้อนโดยผู้ใฃ้ทางแป้นพิมพ์ และแสดงผลพิ้นที่ เส้นรอบ และปริมาตรทางหน้าจอ
#ขอ 5 ฟังก์ชัน
import math
#inputradius
def inputradius():
    r = input('ป้อนรัศมี:')
    #radius = float(input('ป้อนรัศมี:'))
    return input('ป้อนรัศมี:')
#calAreacircle
def calAreacircle(r):
    area = math.pi * r ** 2
    return area

#calRoundcircle
def calRoundcircle(r):
    Roundcircle = 2 * math.pi * r
    return Roundcircle

#calCubecircle
def calCubecircle(r):
    Cube = 4/3 * math.pi * r * r * r
    return Cube

#ShowResult
def ShowResult():
    radius = inputradius()
    area = calAreacircle(radius)
    Roundcircle = calRoundcircle(radius)
    Cube = calCubecircle(radius)
    print("Radius"'%.4f'% radius)
    print("Area"'%.4f'% radius)
    print("Parameter"'%.4f'% radius)
    print(""'%.4f'% radius)