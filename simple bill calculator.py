price = float(input("Price per item: "))
quantity = int(input("How many? "))
total = price * quantity
print(f"{quantity} items at {price:.2f} each = {total:.2f}")