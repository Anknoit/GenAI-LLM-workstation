def multiArraSort(N):
    bigArr = []
    sortArray = []
    for i in range(N):
        arrIn = list(input("User Input ").split())
        bigArr.append(arrIn)
    print("Big Array", bigArr)  # [[1,20,31], [14,15,16]]
    for j in bigArr:  # [1,20,31] [14,15,16]
        for k in j:  # 1,20,31,14,15,16
            sortArray.append(k)  # [1,20,31,14,15,16]
        sortArray.sort()
        print(sortArray)


multiArraSort(2)
