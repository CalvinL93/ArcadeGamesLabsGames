print("This program takes an input of tempurature in Fahrenheit and changes it to Celsius")
temp = input("Input tempurature in Fahrenheit:")

temp = float(temp)
temp = (temp - 32) * (5/9)

print("Tempurature in Celsius:", temp)