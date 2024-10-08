def menu1():
    print("----->>>>> MENU <<<<<-----")
    print("1. Select SQL database.")
    print("2. Select Excel book.")
    print("0. EXIT.")
    while True:
        try:
            x = int(input("Input an option: "))
            if 0<=x<=2:
                return x
            else:
                print("Select an option from the list")
        except ValueError:
            print("Input a true value, between 0 and 2")

def menu2(i):
    while True:
        try:
            x = int(input("Input an option: "))
            if 0<=x<=i:
                return x
            else:
                print("Select an option from the list")
        except ValueError:
            print(f"Input a true value, between 0 and {i}")