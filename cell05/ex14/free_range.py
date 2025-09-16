import sys

def main():
    arr = []
    if len(sys.argv) == 3:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
        # print(num1, num2)
        if num1 > num2:
            for i in range(num1, num2-1, -1):
                arr.append(i)
        else:
            for i in range(num1, num2+1):
                arr.append(i)
        print(arr)
    else:
        print("None")

main()
