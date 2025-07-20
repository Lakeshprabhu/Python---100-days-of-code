import art
def add(n1, n2):
    return n1 + n2

def sub(n1,n2):
    return n1 - n2

def mul(n1,n2):
    return n1*n2

def div(n1,n2):
    try:
        return n1/n2

    except ZeroDivisionError:
        print("Division by zero not possible")

def inputs(skip):
    if skip == False:
        first_number = int(input("Enter the first number:"))
        operator = input("Enter the operation (+,-,*,/):")
        second_number = int(input("Enter the second number:"))
        return first_number,operator,second_number
    else:
        operator = input("Enter the operation (+,-,*,/):")
        second_number = int(input("Enter the second number:"))
        return operator,second_number


def arithmatics(input1,input2,operator):
    operations = {"+":add(input1,input2),"-":sub(input1,input2),"*":mul(input1,input2),"/":div(input1,input2)}
    return operations[operator]

print( art.logo)



def calculator(start,previous_result):


    if start == True:
        input1,operator,input2 = inputs(False)
    else:

        operator,input2 = inputs(True)
        input1 = int(previous_result)





    calculation = arithmatics(input1,input2,operator)

    move_or_clear = (input(f"Do you want to continue with the number {calculation} or start over ? (yes or no) :")).lower()

    if move_or_clear == "yes":

        calculator(False, calculation)

    if move_or_clear == "no":

        print("\n" * 10)
        print(art.logo)
        calculator(True,None)













calculator(True,None)