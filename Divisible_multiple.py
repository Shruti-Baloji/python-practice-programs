# Print m multiples of n where the multiple is not divisble by (n-1) and (n-2) and (n-3)
while True:
    n = int(input("Enter a number"))
    m = int(input("How many multiples do you want to print?"))
    i = n
    count = 0
    while (count < m):
        if ((i % (n-1)) != 0 and (i % (n-2)) != 0 and (i % (n-3)) != 0):
            print(i)
            count += 1
        i += n
        