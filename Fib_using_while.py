while True:
    first = 0
    next = 1
    n = int(input("How many numbers do you want to print?"))
    if n == 0:
       exit 
    else:
        print (first)
        if n > 1:
            print (next)
            while (n > 2): 
                current = first + next
                first = next
                next = current
                print(current)
                n -= 1