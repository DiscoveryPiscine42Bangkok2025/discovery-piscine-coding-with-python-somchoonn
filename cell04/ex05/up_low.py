def up_low(text):
    swp = ""
    for i in text:
        if i.isupper():
            swp += i.lower()
        elif i.islower():
            swp += i.upper()
        else:
            swp += i
    print(swp)
up_low(input("Give me a word: "))