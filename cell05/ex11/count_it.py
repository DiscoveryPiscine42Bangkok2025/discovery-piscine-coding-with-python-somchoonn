import sys

def main():
    num = len(sys.argv)-1
    if len(sys.argv) > 1:
        for i in range(1, num+1):
            print(f"{sys.argv[i]}: {len(sys.argv[i])}")
    else:
        print("None")

main()
