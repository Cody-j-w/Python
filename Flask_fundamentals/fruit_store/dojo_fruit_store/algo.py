def longestPalindrome(string):
    test = ""
    control = ""
    max = ""
    for x in range(0,(len(string))):
            for i in range((len(string))-1, x-1, -1):
                    for j in range(i, x-1, -1):
                            test += string[j]
                    for y in range(x, i+1):
                            control += string[y]
                    if test == control:
                        if (len(test))>(len(max)):
                            max = test
                    else:
                        test = ""
                        control = ""
    return max