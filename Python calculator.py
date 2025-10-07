#python calculator 
while True:
    operator = input("enter an operator (+ - * /) or 'exit' to quit: ")
    if operator == "exit":
        print("Alright, Goodbye!")
        print("🎉 Congratulations on completing your 2nd project!")
        break

    num1 = float(input("enter the first number: "))
    num2 = float(input("enter the second number: "))

    if operator == "+":
        result = num1 + num2
        print(round(result, 2))

    elif operator == "-":
        result = num1 - num2
        print(round(result, 2))


    elif operator == "*":
        result = num1 * num2
        print(round(result, 2))

        
    elif operator == "/":
        result = num1 / num2
        print(round(result, 2))
    else :
        print(f"{operator} is unrecognizable ")
        
    again = input("\nWould u like to continue ? (yes / No): ")

    if again != "yes":
        print("Alright , Goodbye !")
        print("Congratulations on your 2nd project")
        break