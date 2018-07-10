def countdown(x):
     arr = []
     for i in range(x, -1,-1):
             arr.append(i)
     print(arr)

def printReturn(list):
    print(list[0])
    return list[1]

def firstPlus(list):
    sum = list[0] + len(list)
    print(sum)

def greaterThanSecond(list):
    newarr = []
    for x in list:
        if len(list) <= 1:
            return "false"
        if x > list[1]:
            newarr.append(x)
    print(len(newarr))
    return newarr

def lengthAndValue(size, value):
    arr = []
    for x in range(0,size):
        arr.append(size)
    return arr