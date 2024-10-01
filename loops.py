# Write a program that prints all numbers from 1 to 50 that are divisible by 3.

def numb():
    for i in range(1, 51):
        if i % 3 == 0:
            print(i)

numb()