import random

tokens = ["unicorn", "horse", "zebra", "donkey"]
balance = 100

for item in range(0, 20):
    chosen = random.choice(tokens)
    print(chosen, end='\t')

    if chosen == "unicorn":
        balance += 4
    elif chosen == "donkey":
        balance -= 1
    else:
        balance -= 0.5

print("Token: {} , balance: ${}".format(chosen, balance))
