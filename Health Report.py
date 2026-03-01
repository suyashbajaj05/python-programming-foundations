print("--- Suyash's Health App ---")

user_name = input("What is your name? ")
user_gender = input("What is your gender? ")


user_age = int(input("What is your age? "))
weight = float(input("Weight (kg): "))
height_cm = float(input("Height (cm): "))


if user_age <= 13:
    age_msg = "a child"
elif 13 < user_age < 19:
    age_msg = "a teen"
else:
    age_msg = "an adult"


height_m = height_cm / 100
bmi = round(weight / (height_m ** 2), 2)


if bmi < 18.5:
    res = "Underweight\nTip: Focus on nutrition and muscle mass."
elif 18.5 <= bmi < 25:
    res = "Normal weight\nKeep it up!"
elif 25 <= bmi < 30:
    res = "Overweight\nTip: Consider more cardio. Check out Art of Living."
else:
    res = "Obese\nTip: Regular exercise and yoga recommended."


print("\n---------------------------")
print("    YOUR BMI REPORT    ")
print("---------------------------")
print(f"Hello {user_name}!")
print(f"You are {age_msg} ({user_gender}).")
print(f"Your BMI is: {bmi}")
print(f"Category: {res}")
print("---------------------------")
