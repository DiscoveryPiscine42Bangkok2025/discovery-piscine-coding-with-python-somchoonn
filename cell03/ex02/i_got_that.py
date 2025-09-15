def stop():
    print("What you gotta say? : ", end="")
    text = input()
    if text == "STOP":
        pass
    else:
        while True:
            print("I got that! Anything else? : ", end="")
            text = input()
            if text == "STOP":
                break
stop()