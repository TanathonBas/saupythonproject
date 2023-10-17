class test04:
    data1 = 10

    def __init__(self,data2,data3):
        print("Hi....")
        self.data2 = data2
        self.data3 = data3

    def showSumdata(self):
        print(self.data1 + self.data2 + self.data3)
        self.showWow()

    def showWow(self):
        print('WoW wOw WoW....')

objA = test04(10,20)
objB = test04(10,20)
objC = test04(10,100)