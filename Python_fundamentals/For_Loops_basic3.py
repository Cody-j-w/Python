def biggie(arr):
    for x in range(0,(len(list))):
        if list[x] > 0:
            list[x] = "big"
        print(x)

def posiCount(arr):
    arr[-1] = 0
    for x in list:
        if x>0:
            arr[-1] += 1
    print(arr)

def sumTotal(arr):
    sum = 0
    for x in list:
        sum += x
    return sum

def arrAvg(list):
    sum = 0
    for x in list:
        sum += x
    avg = sum/(len(arr))
    return avg

def arrLen(arr):
    length = 0
    for x in list:
        length += 1
    return length

def minimum(list):
    mini = list[0]
    for x in list:
        if (len(list)) == 0:
            return False
        if x<mini:
            mini = x
    return mini

def maximum(list):
    maxi = list[0]
    for x in list:
        if (len(list)) == 0:
            return False
        if x>maxi:
            maxi = x
    return maxi

def ultimateAnalyze(list):
    suma = 0
    mini = list[0]
    maxi = list[0]
    length = 0
    for x in list:
        if (len(list)) == 0:
            return False
        if x > maxi:
            maxi = x
        if x < mini:
            mini = x
        suma += x
        length += 1
    avg = suma/(len(list))
    print("the sum of all values is" + suma)
    print("the average value is" + avg)
    print("the minimum value is" + mini)
    print("the maximum value is" + maxi)
    print("the length of the list is" + length)

def reverseList(list):
    temp = 0
    for x in range(0,(len(list))/2)
        temp = list[x]
        list[x] = list[-(1+x)]
        list[-(1+x)] = temp
    return list