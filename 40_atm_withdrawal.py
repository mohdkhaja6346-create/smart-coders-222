# Problem 40: Atm Withdrawal

balance = float(input("Enter balance: "))
amount = float(input("Enter withdrawal amount: "))
minimum_balance = 500

if amount <= 0:
    print("Invalid amount")
elif amount > balance:
    print("Insufficient balance")
elif balance - amount < minimum_balance:
    print("Minimum balance rule violated")
else:
    print("Withdrawal approved")
    print("Remaining balance =", balance - amount)
