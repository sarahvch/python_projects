from random import randint
num = []
picks = []
choices = [1,2,3]

# generatoe random numbers
for i in choices:
    num.append(randint(0,10))



#weclome and get guesses from users
print("Welcome to the 'Pick a Number' game\nPlease choose three numbers\n\n ")

#while guesses are incorrect
while picks != num:
    guess_1 = input("First Number: ")
    guess_2 = input("Second Number: ")
    guess_3 = input("Thrid Number: ")
    guess_1 = int(guess_1)
    guess_2 = int(guess_2)
    guess_3 = int(guess_3)
    picks = [guess_1, guess_2, guess_3]
    if ((type(guess_1) == int) and (type(guess_2) == int) and (type(guess_3) == int)):
        if (guess_1 == num[0]) or (guess_2 == num[1]) or (guess_3 == num[2]):
            print("\nMatch!")
            if(guess_1 == num[0]):
                print("First Numbers is Correct and in the Correct Place")
            if(guess_2 == num[1]):
                print("Second Number is Correct and in the Correct Place")
            if(guess_3 == num[2]):
                print("Third Number is Correct and in the Corret Place")
        elif((guess_1 in num) or (guess_2 in num) or (guess_3 in num)):
            print("\nClose")
            if(guess_1 in num):
                print("First Numbers is Correct, just not in the Correct Place")
            if(guess_2 in num):
                print("Second Number is Correct, just not in the Correct Place")
            if(guess_3 in num):
                print("Thrid Numbers is Correct, just not in the Correct Place")
        else:
            print("\nNope")

    else:
        print("one of those was not an number, please try again")
if picks == num:
    print("\nYou got it!")
