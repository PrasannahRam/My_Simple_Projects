def prime(n):
    if n == 1:
        print("not a prime number")
    elif n <= 0:
        print("invalid number")
    else:
        j = 2
        while j < n:
            y = n % j
            j = j + 1
            if y == 0:
                print("not a prime")
                break
        else:
            print(n, "is prime number")
    return run()


def run():
    n = int(input("Enter The Number"))
    prime(n)


def password():
    # "password by author#
    pwd = str(2005)
    pwrd = str(input("enter the password"))
    if pwrd == pwd:
        run()
    else:
        print("incorrect password")
        password()


password()
