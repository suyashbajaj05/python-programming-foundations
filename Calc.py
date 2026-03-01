while True:
    a = int(input("\nEnter first number: ")) 
    b = int(input("Enter second number: ")) 
    opr = input("Operation (Add, Subtract, Divide, Multiply): ").capitalize() 

    if opr == "Add":
        print(f"Result: {a + b}")
    elif opr == "Subtract":
        print(f"Result: {a - b}")
    elif opr == "Divide":
        if b != 0:
            print(f"Result: {a / b}")
        else:
            print("Error: Cannot divide by zero.")
    elif opr == "Multiply":
        print(f"Result: {a * b}")
    else: 
        print("Error: Invalid operation.")


    choice = input("\nDo you want to calculate again? (yes/no): ").lower()
    if choice == "no":
        print("Goodbye!")
