import sys

def main():
    num = len(sys.argv)-1
    if len(sys.argv) > 1:
        print(num)
    else:
        print("None")

main()
