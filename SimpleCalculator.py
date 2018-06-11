print("Simple Calculator\n")

while True:
    first_number = input("Enter a number ( or letter to quit): ")
    if not first_number.isdigit():
        break
    first_number = int(first_number)

    operator = input("Enter an operator (+,-,/,*): ")

    second_number = input("Enter another number: ")
    if not second_number.isdigit():
        break
    second_number = int(second_number)
   
    if(operator == "+"):
        first_number += second_number
    elif(operator == "-"):
        first_number -= second_number
    elif(operator == "*"):
        first_number *= second_number
    elif(operator == "/"):
        first_number /= second_number

    print("Result is " + str(first_number))