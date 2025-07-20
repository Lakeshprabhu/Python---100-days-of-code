try:
    age = int(input("How old are you?"))

    if age >= 18:
        print("You can drive at age {age}.")
    elif age <18:
        print(f"{age} years of age is too young , wait till your 18")
    elif age < 1:
        print("You are still an infant")

except Exception:
    print("Enter a valid age")

