#There are 2 inputs. First input is a char, second one is a positive integer. Goal is to generate a patter
pat = input("Enter a character")
n = int(input("Enter an integer"))
for i in range(1,(n+1)):
    for j in range(1,(i+1)):
        print(pat,end = '')
    print("")