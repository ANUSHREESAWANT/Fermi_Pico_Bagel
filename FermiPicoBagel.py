## step 1
import random
original_number = str(random.randint(100,999))  # IN STRING WE CAN COMPARE THE INDEXES BUT NOT IN INT FORM

## create infinite while loop
while True:
## step 2 and step 6
    guess_number = input("Guess the number:") # TO CHECK THE INDEXES OF THE ORIGINAL NUMBER AND THE USER NUMBER WE HAVE USED STRING AND NOT INT
    output = []

## step 3 and step 4 (use continue statement)
    if len(original_number) != len(guess_number):
        print(f'Enter {len(original_number)} digit number') # WE HAVE USED F-STRING SO THAT WE DON'T HAVE TO USE STRING FORMAT (i.e 'Enter' + str(len(original_number)) +'digit number')
        print("Invalid number")
        continue

    if len(guess_number) != len(set(guess_number)):
        print("Duplicate number")
        continue

## step 5 (use break statement for winning condition)
    if guess_number == original_number:    # OR YOU CAN USE int(guess_number) - int(original_number) == 0:
        print("Fermi " * len(original_number))
        print("\nYou won !!")
        break

## step 7
    for i in range(len(original_number)):
        for j in range(len(guess_number)):
            if original_number[i] == guess_number[j]:
                if [i] == [j]:
                    output.append('Fermi')
                else:
                    output.append('Pico')
## step 8
    output_string = ' '
    for item in output:
        output_string = output_string + ' ' + item

## step 9
    if len(output) == 0:
        print("Bagel")
    else:
        print(output_string)