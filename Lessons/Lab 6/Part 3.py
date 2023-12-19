n = int(input("Enter positive number: "))

k = 1
num = 0
for i in range(1, n * 2, 2):
    for j in range(k, n * 2, 2):
        print(j, end=" ")
        num = j
    for j in range(2, k * 2):
        print(" ", end="")
    for j in range(k, n * 2, 2):
        print(num, end=" ")
        num -= 2
    k += 2
    print()

for i in range(1, n * 2, 2):
    k -= 2
    for j in range(k, n * 2, 2):
        num = j
    for j in range(k, n * 2, 2):
        print(j, end=" ")
    for j in range(2, k * 2):
        print(" ", end="")
    for j in range(k, n * 2, 2):
        print(num, end=" ")
        num -= 2
    print()