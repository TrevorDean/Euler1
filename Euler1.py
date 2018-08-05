def multiplefinder35(number):
    counter = 0
    numberstore = []
    while number > 0:
        if number % 3 == 0:
            counter += 1
            numberstore.append(number)
        elif number % 5 == 0:
            counter += 1
            numberstore.append(number)
        number -= 1
    return sum(numberstore)

print multiplefinder35(999)
#Comment

