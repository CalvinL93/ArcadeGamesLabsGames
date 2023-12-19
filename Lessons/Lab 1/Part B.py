print("This program will calculate the area fo a trapezoid with user entered data")

height = input("Enter the height of the trapezoid:")
length_bottom = input("Enter the length of the bottom base:")
length_top = input("Enter the length of the top base:")

height = float(height)
length_bottom = float(length_bottom)
length_top = float (length_top)

area = (1/2) * (length_bottom + length_top) * height

print("The area is:", area)