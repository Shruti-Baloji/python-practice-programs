n = int(input("Enter a positive odd integer"))
spaces_count = int((n-1)/2)
row_count = int((n+1)/2)
for i in range(1,row_count+1):
    for k in range(1, spaces_count+1):
        print(" ",end="")
    spaces_count -= 1
    for j in range(1, 2*i):
        print("*",end="")
    print("")
