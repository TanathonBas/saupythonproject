width = float(input("ป้อนความกว้าง :"))
long = float(input("ป้อนความยาว :"))
high = float(input("ป้อนความสูง :"))
lux = float(input("1 แกลอนทาได้ :"))
print("----------------------------")
area = width*long*high
print("พื้นที่ทั้ง 6 ด้าน {} ตร.ซม จะต้องใช้สี {} แกลอน(แกลอนละ 5 ตร.ซม)". format (width*long*high,round(area/lux)))