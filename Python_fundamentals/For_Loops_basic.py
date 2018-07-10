for i in range (0,151):
    print(i)

for i in range (5, 1000001, 5):
    print(i)

def dojocount(list):
     for x in list:
             if x%5 == 0:
                     if x%10 == 0:
                             x = "Coding Dojo"
                     else:
                             x = "Coding"
             print(x)

def hugesum():
    sum = 0
    for x in range(1,500000,2):
        sum += x
        print(x)
    print(sum)

for x in range(2018,0,-4):
     print(x)

def flexiCount(lowNum,highNum,mult):
     for x in range(lowNum, highNum, mult):
             print(x)

