def calculate_sellingprice(costprice):
    sellingprice = costprice + (costprice * 10/100)
    return sellingprice

def productinfo():
    productname = input("ป้อนชื่อสินค้า: ")
    costprice = float(input("ป้อนราคาสินค้า: "))
    return productname, costprice

def result(productname,sellinprice):
    print(f'สินค้า {productname}')
    print(f'ราคา {sellinprice:.2f} บาท')

productname, costprice = productinfo()
sellingprice = calculate_sellingprice(costprice)

result(productname,sellingprice)
