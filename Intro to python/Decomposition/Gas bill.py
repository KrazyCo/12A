class GasBill:
    def __init__(self, gasPrice=5, standingCharge=20):
        self.oldReading = 1890
        self.currentBalance = 50
        self.gasPrice = gasPrice
        self.standingCharge = standingCharge

    def getReading(self):
        validInput = False
        while not validInput:
            reading = input("Enter the reading on the gas meter: ")
            if reading.isnumeric():
                if int(reading) > self.oldReading:
                    validInput = True
            if not validInput:
                print("Impossible reading")
        return int(reading)

    def calcuateBalance(self, meterReading):
        newGas = meterReading - self.oldReading
        self.currentBalance -= self.gasPrice * newGas + self.standingCharge
        if self.currentBalance < 0:
            bill = 0 - self.currentBalance
            self.currentBalance = 0
        else:
            bill = 0
        return bill

    def generateBill(self, bill):
        print(f'''You gas bill is: £{round(bill, 2)}
Your current balance is £{round(self.currentBalance, 2)}''')


gasBill = GasBill()
reading = gasBill.getReading()
bill = gasBill.calcuateBalance(reading)
gasBill.generateBill(bill)
