import sys

def downcase_it(string):
    return string.lower()
def main():
    if len(sys.argv) == 1:
        print("None")
    else:
        for arg in sys.argv[1:]:
            print(downcase_it(arg))

main()