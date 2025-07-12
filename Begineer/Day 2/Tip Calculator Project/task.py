print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))


tip_percent = tip/100
tip = bill* tip_percent
total_bill = (bill+ tip)/people
round(total_bill,2)
print(f"{total_bill}")