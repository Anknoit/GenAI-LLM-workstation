def search_position(arr, N, X):
    if len(arr) == N:  # No. of elements in array
        if X in arr:  # Checking if X is in array
            print(arr.index(X))  # printing the index value of X element
            # return arr.index(X)
        else:
            print("-1")
            # return -1


search_position([1, 2, 3, 4], 4, 7)
