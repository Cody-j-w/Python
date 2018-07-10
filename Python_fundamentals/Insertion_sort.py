def insertionSort(list):
    for x in range(0,(len(list))):
        temp = 0
        for i in range(x, 0, -1):
            if list[i-1]<list[i]:
                break                    
            temp = list[i]
            list[i] = list[i-1]
            list[i-1] = temp
    print(list)
