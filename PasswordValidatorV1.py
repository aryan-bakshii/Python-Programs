symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', ';', ':']
lower_case = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper_case = list(map(str.upper, lower_case))
digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

while True:
    hasSymbol = False
    hasCapital = False
    minLength = False
    hasNumber = False

    password = list(input('Enter your password > '))
    for element in password:
        if element in symbols and hasSymbol is False:
            hasSymbol = True
        if element in upper_case and hasCapital is False:
            hasCapital = True
        if element in digits and hasNumber is False:
            hasNumber = True

    if len(password) >= 8:
        minLength = True

    if minLength and hasNumber and hasCapital and hasSymbol:
        print("""Password passed all validations.\nPassword saved successfully.""")
        break
    else:
        print("Please enter a valid Password.")
        continue
