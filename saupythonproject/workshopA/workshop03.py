def calculatetax(price):
    tax = price * 0.07
    return tax

def productinfo():
    productname = input("ป้อนชื่อสิค้า: ")
    productprice = float(input("ป้อนราคาสินค้า: "))
    return productname, productprice

def result(productname,productprice,tax):
    print(f'สินค้า {productname}')
    print(f'ราคา {productprice:.2f}บาท')
    print(f'ภาษีที่ต้องจ่าย {tax:.2f}บาท')

productname, productprice = productinfo()
tax = calculatetax(productprice)
result(productname,productprice,tax)