def table(num):
    for i in range(0, 10):
        print(f"{i} x {num} = {i * num}")

print("Enter a number: ")
num = int(input())
table(num)
