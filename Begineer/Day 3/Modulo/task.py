print( 10 % 3) # 1

user_input = int(input("Enter the number to be checked :"))
check = user_input % 2
if check == 0:
    print(f"The number is even ({user_input})")
else:
    print(f"The number is odd ({user_input})")