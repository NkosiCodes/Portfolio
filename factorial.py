# Create a program that calculates the factorial of a number using a for loop.

# example of a factorial 6! = 6 * 5 * 4 * 3 * 2 * 1 = 720
# mathematically  n = n + n -1
#                 n! = n × (n−1)!

#  problem is we don't know what the nth term might be now 
#  I must find a way to make this work somehow but when we 
#  prove it and test it mathematically it must make sense too

#    (6 - 1) * (6 - 2) * (6 - 3) * (6 - 4) * (6 - 5) = 720


# num = int(input("write factorial: "))

# factorial = 0

# for i in range(1, num):
#     for j in range(i):
#       factorial = (num * i)*j * (num - i)**j+i
#     print(factorial)

## if 5 then 5 * 4 * 3 * 2 * 1 = 360

# hahaha ChatGpt solved this one again, turns out it was sooo stupidly easy to solve
# proves that I must get back to practising my maths hahaha

num = int(input("Enter a number to calculate its factorial: "))

# Start with 1 since factorial multiplies numbers
factorial = 1

# Loop to multiply numbers from 1 to num
for i in range(1, num + 1):
    factorial *= i  # This is equivalent to factorial = factorial * i

# Print the result
print(f"The factorial of {num} is {factorial}")
