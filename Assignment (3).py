numbers = [-12, 4, 12, 25, 67]

while True:
    number = int(input("Enter a number (or enter -99 to quit): "))
    if number == -99:
        break
    numbers.append(number)
    numbers.sort()
    print(numbers)