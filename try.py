rows = 4  # Number of rows in the pattern

for i in range(1, rows + 1):
   num = i  # Start each row with the current row number
   for j in range(1, i + 1):
       print(num, end="")  # Print the number without a newline
       num += 1  # Increment the number for the next iteration
   print()  # Move to the next line after each row