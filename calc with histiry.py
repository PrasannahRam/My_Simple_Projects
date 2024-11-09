def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b != 0:
        return a / b
    else:
        print("float division by zero")


def power(a, b):
    return a ^ b


def remainder(a, b):
    return a % b


def check(x):
    op(x)
    print(x)
    try:
        float(x)
    except:
        print("enter a valid number")
        run()


def history():
    if 0 == len(history_list):
        print('No past calculations to show')
    else:
        for x in history_list:
            print(x)


def select_op_for_calc(choice, a, b):
    if choice == "+":
        return add(a, b)
    if choice == "-":
        return subtract(a, b)
    if choice == "*":
        return multiply(a, b)
    if choice == "/":
        return divide(a, b)
    if choice == "^":
        return power(a, b)
    if choice == "%":
        return remainder(a, b)


def op(choice):
    if choice == "?":
        history()
        run()
    if choice == "$":
        run()
    elif choice == "#":
        # program ends here
        print("Done. Terminating")
        exit()
    else:
        return


def run():
    print("Select operation.")
    print("1.Add      : + ")
    print("2.Subtract : - ")
    print("3.Multiply : * ")
    print("4.Divide   : / ")
    print("5.Power    : ^ ")
    print("6.Remainder: % ")
    print("7.Terminate: # ")
    print("8.Reset    : $ ")
    print("8.History  : ? ")
    choice = input("Enter choice(+,-,*,/,^,%,#,$,?): ")
    print(choice)
    if choice not in ["+", "-", "*", "^", "%", "#", "$", "?", "/"]:
        print("invalid operation")
        run()
    op(choice)
    a = input("Enter first number: ")
    check(a)
    b = input("Enter second number: ")
    check(b)
    a = float(a)
    b = float(b)
    res = ("{0} {1} {2} = {3}".format(float(a), str(choice), float(b), (select_op_for_calc(choice, a, b))))
    print(res)
    history_list.append(res)
    run()



history_list = []
run()
