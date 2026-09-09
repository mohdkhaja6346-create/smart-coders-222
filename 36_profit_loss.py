# Problem 36: Profit Loss

cost = float(input("Enter cost price: "))
sell = float(input("Enter selling price: "))

if sell > cost:
    print("Profit =", sell - cost)
elif cost > sell:
    print("Loss =", cost - sell)
else:
    print("No profit, no loss")
