from random import randint

def lotto():
    numbers = []
    draw = []
    hit = 0
    while len(numbers) < 6:
        try:
            number = input("Input number form range 1-49: ")
            number = int(number)
            if number not in range(1, 50):
                print("Out of range")
                continue
            if number in numbers:
                print("Number exist")
                continue
            numbers.append(number)
        except ValueError:
            print("This is not a natural number")
            continue
    numbers.sort()
    for k in range(6):
        draw.append(randint(1, 49))
    draw.sort()
    print("Drawn numbers: ", draw)
    for i in range(6):
        if numbers[i] in draw:
            hit += 1
    if hit >= 3:
        result = f"You have chosen {hit} correct numbers. Congrats."
    else:
        result = "Sorry, you lost. Try again."

    return result

print(lotto())