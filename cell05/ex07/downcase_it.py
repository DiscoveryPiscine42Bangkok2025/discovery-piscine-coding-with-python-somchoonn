import sys

def main():
    if len(sys.argv) > 1:
        print(str(sys.argv[1]).lower())
    else:
        print("None")

main()
