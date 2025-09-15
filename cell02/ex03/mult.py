print("Enter the first number:")
num1 = int(input())
print("Enter the second number:")
num2 = int(input())
print("%d x %d = %d"%(num1, num2, num1 * num2)) 
if num1*num2 < 0:
    print("This number is negative.")
elif num1*num2 > 0:
    print("This number is positive.")
else:
    print("This number is both postive and negative.")