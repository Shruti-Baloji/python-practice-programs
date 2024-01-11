N = int(input("Enter a positive integer"))
for i in range(1,(int((N+1)/2)+1)):
    for j in range(1,2*i):
        print("*",end="")
    print("")
