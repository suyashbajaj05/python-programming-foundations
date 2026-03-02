name = input("What's your name?: ").lower().strip()
style = input("What are you wearing? (Suits, Tshirt, Hoodie): ").lower().strip()
wallet = int(input("How much money do you have?: "))

if name == "suyash":
    print("Oh! Trillionaire Businessman! Welcome to the club, we have been waiting for you, Sir!")

elif style == "tshirt" and wallet >= 100:
    print("Hey buddy, not today, come in suits, for now, maybe Bar fits you, if you're 18+")

elif style == "suits":
    print("Welcome! VIP, We were waiting for you!")

else:
    print("Sorry, you can't enter the club, maybe try again with a different style or more money?")