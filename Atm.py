from hashlib import new


class ATM:
    def __init__(self, cardNumber, pinNumber):
        self.cardNumber = cardNumber
        self.pinNumber = pinNumber
    def BalanceEnquiry(self):
        print("Your balance is 100000")
    def CashWithdrawal(self, amount):
        newAmount = 100000 - amount
        print("Your balance after withdrawal is ", newAmount)
cardNumber = input("Enter your card number")
pinNumber = input("Enter your pin number")
newUser = ATM(cardNumber, pinNumber)
print("Choose your activity")
print("1. BalanceEnquiry    2. CashWithdrawal")
activity = int(input("Enter your activity number"))
if activity == 1:
    newUser.BalanceEnquiry()
elif activity == 2:
    amount = int(input("Enter the amount you want to withdraw"))
    newUser.CashWithdrawal(amount)
else:
    print("Enter a valid number")