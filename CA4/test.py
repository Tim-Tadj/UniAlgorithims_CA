def echo(string1):
    print("Echo:", string1)
while True:
    x = input("Put your input here: ")
    if x == "q" or x == "shut up":
        print("sorry :(")
        quit()
    echo(x)