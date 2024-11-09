

def prime_factors():
    num = int(input("enter the number"))
    factors = []
    divider = 2
    while num >= divider:
        if num % divider == 0:
            factors.append(divider)
            num = num / divider
        else:
            divider = divider + 1

    print(factors)
    prime_factors()


prime_factors()
