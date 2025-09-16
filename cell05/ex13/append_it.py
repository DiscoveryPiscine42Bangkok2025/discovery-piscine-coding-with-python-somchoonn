import sys

def main():
    num = len(sys.argv)-1
    if len(sys.argv) > 1:
        for i in range(1, num+1):
            if sys.argv[i][-3:] != "ism":
                print(f"{sys.argv[i]}ism")
    else:
        print("None")

main()
