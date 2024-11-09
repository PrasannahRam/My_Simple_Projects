def find_date():
    start = input("""Press Enter To Gets Started or Type "exit" To Exit""")
    if start == "exit":
        exit("closing")
    year = int(input("YEAR"))
    month = int(input("MONTH"))
    date = int(input("DATE"))

    days_in_month = 0
    n = 1
    while n < month:
        if n in [1, 3, 5, 7, 8, 10, 12]:
            days_in_month += 31
        elif n in [4, 6, 9, 11]:
            days_in_month += 30
        elif n == 2:
            days_in_month += 28
            if year % 4 == 0:
                days_in_month += 1
        n += 1

    days = int((year - 1905) * 365) + int((year - 1905) / 4) + days_in_month + date

    name_of_days = ['SUNDAY', "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY"]
    print("It's a "+name_of_days[(days % 7) - 1])
    find_date()


find_date()
