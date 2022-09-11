import random

def statement_generator(statement, decoration):

    sides = decoration * 3

    statement = "{} {} {} ".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""

statement_generator("Welcome to the Lucky Unicorn Game", "*")
print()

def yes_no(question):
   valid = False
   while not valid:
       response = input(question).lower()

       if response == "yes" or response == "y":
           response = "yes"
           return response

       elif response == "no" or response == "n":
           response = "no"
           return response

       else:
           print("Please answer with yes/no or y/n")


def instructions():
   print("**** How to play ****")
   print()
   print("Choose a Starting amount (Minimum $1, Maximum $10).")
   print()
   print("Then press <Enter> to play. you will get either a horse, a zebra, a donkey or a unicorn.")
   print()
   print("It costs a $1 per round.   Depending on your prize you might win some of the money back.   Here's the payout amounts...")
   print("Unicorn: $5.00 (Balance increases by $4)")
   print("Horse: $0.50 (Balance decreases by $0.50)")
   print("Zebra: $0.50 (Balance decreases by $0.50)")
   print("Donkey: $0.00 (Balance decreases by $1)")
   print()
   print("Can you avoid the donkeys, get the unicorns and walk home with the money??")
   print()
   print("Hint: to quit while you are ahead, type 'xxx' instead of pressing <Enter>")


   print()
   return ""

played_before = yes_no("Have you played this game before? ")


if played_before == "no":
   instructions()

print("Program continues")
def num_check(question, low, high):
   error = "Please enter an whole number between 1 and 10\n"

   valid = False
   while not valid:
       try:
           response = int(input(question))
           if low < response <= high:
               return response


           else:
               print(error)
       except ValueError:
           print(error)


how_much = num_check("How much would you like to play with? ", 0, 10)

balance = how_much

rounds_played = 0

play_again = input("Press <Enter> to play.... ")
while play_again == "":

    rounds_played += 1
    print()
    print("*** Round: #{} *** ".format(rounds_played))

    chosen_num = random.randint(1, 100)

    if 1 <= chosen_num <= 5:
        chosen = "Unicorn"
        balance += 4

    elif 6 <= chosen_num <= 36:
        chosen = "donkey"
        balance -= 1

    else:
        if chosen_num % 2 == 0:
            chosen = "Horse"

        else:
            chosen = "Zebra"

    balance -= 0.5
    print("You got a {}. Your balance is " " ${:.2f}".format(chosen, balance))
    print()

    if balance < 1:
        play_again = "xxx"
        print("Sorry you have run out of money")
    else:
        play_again = input("Press Enter to play again " "or 'xxx' to quit")


print()
print("Final Balance is ${}".format(balance))

