row = int(input("Enter no. of rows: "))

for i in range(row):
    for j in range(row-i): #range(i,n)
        print("*", end=" ")
    print()