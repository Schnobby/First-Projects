import numpy as np

# define function to test for wrong userinputs. User has to write integer between 1 and 10
def inputnumber(num):
    while True:
        try:
           number = int(input(num))
        except ValueError:
           print("Your guess has to be an integer between 1 and 10! Try again.")
           continue
        else:
           if number <= 0 or number >= 11:
               print("Your guess has to be between 1 and 10! Try again.")
               continue
           else:
               return number

# Create random Number between 1 and 20
c_num = np.random.randint(1,11)
print("The computer chose a number between 1 and 10.")
# Ask User for Guess
u_num = inputnumber("What is your guess?: ")
print("The computer chose: " + str(c_num))
print("You chose: " + str(u_num))

# Test userinput against computer generated number
if u_num == c_num:
    print("Your guess was right! Congratulations!")
elif u_num > c_num:
    print("Sorry, the right answer was " + str(c_num) + ". Your guess was too high!")
elif u_num < c_num:
    print("Sorry, the right answer was " + str(c_num) + ". Your guess was too low!")

print("Thank you for playing!")