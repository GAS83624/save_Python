import random

x = random.randint(1, 1000)
print("========")
print("เฉลยคำตอบ =",x)
print("========")
while True:
    num = int(input("Guess the number between 1 and 1000: "))

    if num == x:
        print("Congratulations! You guessed the number!")
        break
    elif num < x:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")