# Benjamin McDaniel
# BDO Cooking Calculator

# import locale to format thousands ","
import locale
locale.setlocale(locale.LC_ALL, '')  # Use '' for auto, or force e.g. to 'en_US.UTF-8'


# user input
bPrice=input("Enter price of one box: ")
bAmount=input("Enter Contributions Amount: ")
bBonus=input("Enter Bonus Multiplier % in decimal: ")
    
    
amountPerBox=((int(bPrice) * float(bBonus)) + int(bPrice)) #price per box
totalTurnIn=amountPerBox*float(bAmount) # total turn in per day
    
total_in_week=totalTurnIn*7 # total week    
total_in_month=total_in_week*4 #total month

#output
print("\nTurn in Amount Daily: " + bAmount)
print("\nTotal Silver per Day: " + f"{totalTurnIn:,}")
print("Total Silver per Week: " + f"{total_in_week:,}")
print("Total Silver per Month: " + f"{total_in_month:,}")