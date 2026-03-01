#Username & Password Checker
#Ask username, contact number and password from the user
username = input("Enter your username: ")
print(f"Hello, {username}!")
Contact = input("Enter your contact number: ")
password = input("Enter your password: ")
#Check if password is correct and display Yes or No
if password == f"{username}@{Contact}":
    print("Login successful!")
    YoN = input(f"{username}, Do you want to access your document? (yes/no): ").lower()
    if YoN == "yes":
        print("Accessing your document...")
        print("link:" f"https://www.{username}doc.com")
    elif YoN == "no":
        print("Okay, have a great day!")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
#Incorrect password output
else:
    print("Login failed. Incorrect password.")
