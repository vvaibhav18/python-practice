
a = input("Enter Item_Name")
b = float(input("Enter Unit price"))
c= int(input("Enter Quantity"))
d = float(input("Enter Tax rate"))

subtotal = b * c
tax = subtotal * d / 100
total = subtotal + tax

print("Product:",a)
print("Quantity:",c)
print("Unit Price:",b)
print("Subtotal:",subtotal)
print(f"tax ({d}%)",tax)
print("Total Payable:",total)