# A program to print n multiples of 7
i = 0
while True:
    n = int(input("Enter a number"))
    while (n > 0):
        i += 7
        print(i)
        n -= 1