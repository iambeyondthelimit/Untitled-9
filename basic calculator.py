def addition(num1, num2):
    return num1 + num2
    
def subtraction(num1, num2):
    return num1 - num2
    
def multiplication(num1, num2):
    return num1 * num2
    
def division(num1, num2):
    return num1 / num2

    
while True:
    try:
        print("-----Basic Calculator-----")
        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter a number: "))
        operation = input("Choose operation (+, -, *, /): ")
        if operation == "+": 
            print("result: ", num1, "+", num2, "=", addition(num1,num2))
        elif operation == "-": 
            print("result: ", num1, "-", num2, "=", subtraction(num1,num2))
        elif operation == "*": 
            print("result: ", num1, "*", num2, "=", multiplication(num1,num2))
        elif operation == "/": 
            if num2 == 0:
                print("Error! cannot divide by 0 number.")
            else:
                print("result: ", num1, "/", num2, "=", division(num1,num2))
    except ValueError:
        print("Invalid input. Try again!")
