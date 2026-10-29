import random 
secret = random.randint(1, 100)
attempts = 0
found = False

while attempts < 7:
    guess = int(input("Your guess: "))
    attempts = attempts + 1

    if guess == secret:
        print(f"Bravo! Found in {attempts} atempts")
        found = True
        break
    elif guess < secret:
        print("Too low!")
    else:
        print("Too high!")

if not found:
    print(f"Lost! The secret was {secret}")