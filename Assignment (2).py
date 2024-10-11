Names = ["Maria", "Hala", "Ghady", "Ehsan", "Joe", "Zoe"]

while True:
    letter = input("Enter a letter (Or \"exit\" to stop): ")
    if letter == "exit":
        break
    if len(letter) != 1 or not letter.isalpha():
        print("Wrong input")
        continue
    letter = letter.lower()
    for name in Names:
        if letter in name.lower():
            print(name)
        


