n = int(input("Number for box size: "))

for i in range(0, n * 2):
    print("o", end="")

for i in range(0, n - 2):
    print("\no", end="")
    for j in range(0, (n * 2) - 2):
        print(" ", end="")
    print("o", end="")
print()

for i in range(0, n * 2):
    print("o", end="")