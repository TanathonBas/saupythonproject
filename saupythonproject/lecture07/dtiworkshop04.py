def calculate(x):
    y = 2 * x**2 + 2 * x + 1
    return y

def inputx():
    x = float(input("ป้อนค่า x :"))  
    return x

def result(x,y):
    print(f'ค่า x: {x}')
    print(f'ค่า y: {y}')

x = inputx
y = calculate(x)

result(x,y)