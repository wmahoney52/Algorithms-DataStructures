"""
Change Maker Template
Create a simple Cashier system that asks the user to enter an amount being paid
and gives back correct change based on the initial cost, and displays the different
denominations that were used to give back the change.
"""
import random

#Ask for users first and last name seperately.
user_first_name = input("Enter your first name: ")
user_last_name = input("Enter your last name: ")

#Print a greeting.
print("Welcome, " + user_first_name + ".")

"""
Randomly generated number for the amount to be paid.
This value is in PENNIES
DO NOT ALTER
"""
amount_to_be_paid = int(100.00 + (random.random() * (10000.00 - 100.00)))

#Ask for users payment amount. This should be stored in a variable as dollars.
while True:
	print("Total: " + "${:,.2f}".format(amount_to_be_paid / 100))
	try:
		user_amount_paid = float(input("Enter amount to pay with: "))
		if user_amount_paid > amount_to_be_paid / 100:
			break
		print("You need to pay with more money. " + str(user_amount_paid) + " is not enough to provide change. TRY AGAIN")
	except ValueError:
		print("You need to enter a dollar amount above the total price. TRY AGAIN")

#Calculate amount of change that should tendered.
change_given = (user_amount_paid * 100) - amount_to_be_paid
print("Your change is: " + "${:,.2f}".format(change_given / 100))

#Calculate amount of every denomination that should be given.
change_denominations = {2000:0, 1000:0, 500:0, 100:0, 25:0, 10:0, 5:0}

for denomination in change_denominations:
	change_denominations[denomination] = change_given // denomination
	change_given %= denomination

num_pennies = change_given

#Print all information in a meaningful, readable manner.
print("I paid you with: ")

for denomination in change_denominations:
	print("    ${:,.2f}".format(denomination / 100) +  "'s: " + str(int(change_denominations[denomination])))
print("    $0.01's: " + str(int(num_pennies)))

print("GOOD DAY & GOODBYE")
