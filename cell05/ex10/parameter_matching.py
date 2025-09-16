import sys

def main():
    if len(sys.argv) != 2:
        print("None")
        return

    param = sys.argv[1]
    user_input = input(f"What was the parameter? ")

    if user_input == param:
        print("Good job!")
    else:
        print("Nope, sorry...")

main()
