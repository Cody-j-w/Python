def selectionSort(list):
    for x in range(0, (len(list))):
        min = list[x]
        marker = x
        for i in range (x, (len(list))):
            if min>list[i]:
                min = list[i]
                marker = i
        list[x], list[marker] = list[marker], list[x]
    print(list)