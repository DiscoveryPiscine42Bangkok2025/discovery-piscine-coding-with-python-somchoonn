import sys

def main():
    if len(sys.argv) > 1:
        print(str(sys.argv[1]).upper())
    else:
        print("None")

main()
