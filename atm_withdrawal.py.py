 # Interactive Scientific Temperature Converter


withdrawal_amount = int(input("number"))
remaining = withdrawal_amount

note_500 = remaining // 500
remaining %= 500 

note_200 = remaining // 200
remaining %= 200

note_100 = remaining // 100
remaining %= 100

note_50 = remaining // 50
remaining %= 50

note_10 = remaining // 10
remaining %= 10


print("withdrawal_amount:",withdrawal_amount )
print("note_500:",note_500 )
print("note_200:",note_200 )
print("note_100:",note_100)
print("note_50:",note_50)
print("note_10:",note_10)
print("Remaining Undispensed:",remaining)