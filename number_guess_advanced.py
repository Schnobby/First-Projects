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


# Count number of tries

t_num = 1

# Create random Number between 1 and 20
c_num = np.random.randint(1,11)
print("The computer chose a number between 1 and 10.")

# Ask User for Guess
u_num = inputnumber("What is your guess?: ")

# Test userinput against computer generated number
while u_num != c_num:
    if u_num > c_num:
        t_num = t_num + 1
        print("Sorry, the right answer is lower. Your guess was too high! Try again!")
        u_num = inputnumber("What is your new guess?:")
    elif u_num < c_num:
        t_num = t_num + 1
        print("Sorry, the right answer is higher. Your guess was too low! Try again!")
        u_num = inputnumber("What is your new guess?:")

print("Your guess was right on try: " + str(t_num) + "! Congratulations!")
print("Thank you for playing!")