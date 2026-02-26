Bot = "again"
while Bot == "again":
    Name = input("what is your name? ")
    Digit = int(input(f"Hello {Name.capitalize()}. Welcome to the odd or even number checker bot. Enter a number: "))
    if Digit % 2 == 0:
        print(f"{Name.capitalize()}, the number {Digit} is an even number.")
    else:
        print(f"{Name.capitalize()}, the number {Digit} is an odd number.")

    Bot = input("Type 'again' to continue: ")

print("End of program.")