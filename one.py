# Write a program that converts 
# temperature from Celsius to Fahrenheit and vice versa

Conv = input("Convert to Celsius or to Farenheit?: ")
if Conv == "Farenheit":
    Cel = float(input("Amount: "))

    farc = (Cel * 9/5) + 32

    print(farc, "degrees Farenheit")

elif Conv == "Celsius":
    Far = float(input("Amount: "))

    farc = (Far - 32) * 5/9

    print(farc, "degrees Celsius")