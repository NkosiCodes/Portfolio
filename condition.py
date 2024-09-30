# Write a program that checks if a number is even or odd.

# input of type integer
num = int(input("Type in your number: "))

# checks if input divided by 2 does not return a remainder
# hence num divided by 2 equals 2
if num % 2 == 0:
    print("This is an even number: ", num, " Remainder: ", num % 2)

# checks if input divided by 2 does return a remainder
# hence if num divided by 2 is not equal to 0 that means it returns a remainder
elif num % 2 != 0:
    print("This is an odd number: ", num, " Remainder: ", num % 2)


#ChatGpt's version 
# I only use it to check for errors and improve my code
# and for effective learning

# input of type integer
num = int(input("Type in your number: "))

# checks if input divided by 2 returns a remainder of 0
if num % 2 == 0:
    print("This is an even number:", num, "Remainder:", num % 2)
else:
    print("This is an odd number:", num, "Remainder:", num % 2)
