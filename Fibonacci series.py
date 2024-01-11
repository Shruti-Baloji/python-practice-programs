#Fibonacci series
while True:
    first = 0
    next = 1
    n = int(input("How many numbers do you want to print?")) #n = 3, 0 , 1, 1
    if n == 0:
       exit 
    elif n == 1:
        print(first)
    else:
        print (first)
        print (next)
        for i in range(1,n-1): #i = 1, current = 1
            current = first + next
            first = next
            next = current
            print(current)