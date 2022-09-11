import random

tokens = ["Unicorn", "Horse", "Horse", "Horse", "Zebra", "Zebra", "Zebra", "Donkey", "Donkey", "Donkey"]
STARTING_BALANCE = 100

balance = STARTING_BALANCE
for item in range(0, 500):
    chosen = random.choice(tokens)

    if chosen == "unicorn":
        balance += 4
    elif chosen == "donkey":
        balance -= 1
    else:
        balance -= 0.5

print()
print("Starting balance: ${:.2f}".format(STARTING_BALANCE))
print("Final balance: ${:.2f}".format(balance))
