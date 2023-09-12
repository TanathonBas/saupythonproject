def inputbasehigh():
    base = input("ป้อนฐาน:")
    high = input("ป้อนสูง:")
    return base, high

def calAndShowtrianglearea (base, high):
    area = base * high / 2
    print(f"สามเหลี่ยมฐาน{base:.2f} สูง {high:.2f} มีพื้นที่ {area:.2f}")

print("----------------------------")
print("calculate triangle Area")
print("----------------------------")
base, high = inputbasehigh()
print("----------------------------")
calAndShowtrianglearea (base, high)
print("----------------------------")