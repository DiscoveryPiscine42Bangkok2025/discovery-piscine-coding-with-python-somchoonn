def check(num):
    # print(num.is_integer())
    if num.is_integer():
        print("The number is integer.")
    else:
        print("The number is decimal.")
check(float(input("Give me a number: ")))