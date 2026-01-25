T = int(input())
for i in range(T):
    N, K = map(
        int, input().split()
    )  # N= No. of elements for the array, K = index position from where array will be rotated
    arr = list(input().split())  # array of N elemets
    print(type(N), type(K), type(arr))
    # print(len(arr))
    if len(arr) <= N:
        # Write shit here
        new_arr = arr[-K:] + arr[:-K]

print(" ".join(new_arr))
