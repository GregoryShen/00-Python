import random

num = random.randint(1, 100)


while True:
    try:
        guess = int(input("Enter 1~100:"))
    except ValueError as e:
        print("Enter 1~100!")
        continue
    if guess > num:
        print("guess Bigger:", guess)
    elif guess < num:
        print("guess smaller:", guess)
    else:
        print("guess ok, game over")
        break
print("\n")
