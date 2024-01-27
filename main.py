print("Welcome to the Tip Calculator")

bill = float(input("What was the total bill?\n$"))
percentage = float(input("What percetntage tip you want to give? 10, 12, 15\n")) 
people = int(input("How many people to split the bill?\n"))
net_percentage = float(percentage / 100)
tip = (bill / people) * net_percentage
round_tip = format(tip, '.2f')
payable_bill = bill / people + tip
total_bill = format(payable_bill, '.2f')
print(f"Each Person Should pay: {total_bill}$, Tip will be: {round_tip}$ for each person.")