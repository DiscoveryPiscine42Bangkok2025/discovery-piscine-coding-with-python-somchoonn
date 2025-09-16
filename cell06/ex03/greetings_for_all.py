def greetings(string=None):
    if isinstance(string, str):
        print(f"Hello, {string}!")
    elif string is None:
        print("Hello, noble stranger.")
    else:
        print("Error! It was not a name.")
        

greetings("Alexandra")
greetings("Will")
greetings()
greetings(42)
