def calculator(num1,num2):
    print("Thank you!")
    print(f"{num1} + {num2} = {num1 + num2}")
    print(f"{num1} - {num2} = {num1 - num2}")
    print(f"{num1} / {num2} = {num1 // num2}")  
    print(f"{num1} * {num2} = {num1 * num2}")

calculator(int(input("Give me the first number: ")), int(input("Give me the second number: ")))