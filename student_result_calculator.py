a = int(input("Enter English Marks:"))
b = int(input("Enter Mathematics Marks:"))
c = int(input("Enter physics Marks:"))
d = int(input("Enter Chemistry Marks:"))
e = int(input("Enter Python Marks:"))

Total_marks=(a+b+c+d+e)
print("Total Marks:",Total_marks)
percentage=(Total_marks/500*100)
print("percentage:",percentage)

if percentage >=90 and percentage <=100 :
    print("Grade :" "A+")
    print("Result :" "Pass")


elif percentage >=80 and percentage <=89 :
    print("Grade:" "A")
    print("Result:" "Pass")



elif percentage >=70 and percentage <=79 :
     print("Grade:" "B")
     print("Result:" "pass")


elif percentage >=60 and percentage <=69 :
    print("Grade:" "C")
    print("Result:" "Pass")


elif percentage >=40 and percentage <=59 :
    print("Grade:" "D")
    print("Result:" "Pass")