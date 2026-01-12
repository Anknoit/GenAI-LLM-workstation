def arr_rev(N):
    newArr = []
    for i in range((len(N) - 1), -1, -1):  # Backward loop
        newArr += N[i]  # appending/adding elements of N backwards using backward loop
    # print(newArr)
    print(" ".join(newArr))
    return " ".join(newArr)


arr_rev("Hi Iam Ankit Jha!")
