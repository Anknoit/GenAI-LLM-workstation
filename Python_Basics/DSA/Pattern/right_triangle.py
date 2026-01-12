row = int(input("Enter no. of rows:"))

for i in range(row):
    for j in range(i+1):
        print("*" , end="")
        # print(" " * i, end="")
    
    print()