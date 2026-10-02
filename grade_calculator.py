num = int(input("Enter Percentage"))

if num >= 90 and num<= 100:
  print("A+ Grade")

elif num >=80 and num <=89:
  print("A grade")

elif num >=70 and num <=79:
  print("B grade")

elif num >=60 and num <=69:
  print("C grade")

elif num >=40 and num <=59:
  print("D grade")

elif num < 40:
  print("F grade")

else:
  print("invalid grade")