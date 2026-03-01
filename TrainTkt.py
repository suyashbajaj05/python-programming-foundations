# Train Ticket Price Calculator
#Ask user their age and the original ticket price
age = int(input("What is your age?: "))
tp = float(input("What was original ticket price?: "))
#Calculate the ticket price based on the age of the user and print the result rounded to 2 decimal places
if 0 < age < 18:
    print("Your ticket price is: ", (round(tp * 0.5, 2)))
elif 18 <= age <= 26: 
    print("Your ticket price is: ", (round(tp * 0.75, 2)))
elif age >= 65:
    print(f"Your ticket price is: ", (round(tp * 0.6, 2)))
elif 26 < age < 65:
    print("Your ticket price is: ", round(tp, 2))
else:
    print("Invalid input")