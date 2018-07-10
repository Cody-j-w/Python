def bracesValid(string):
    newstr = 'i'
    i = 0
    for x in range(0,(len(string))):
            if string[x] == '(' or string[x] == '[' or string[x] == '{':
                    newstr += string[x]
                    i += 1
                    print(i)
            if string[x] == ')':
                    print(newstr)
                    print(i)
                    if newstr[i] == '(':
                            newstr[:-1]
                            i -+ 1
                    else:
                            return False
            if string[x] == '}':
                    print(newstr)
                    print(i)
                    if newstr[i] == '{':
                            newstr[:-1]
                            i -=1
                    else:
                            return False
            if string[x] == ']':
                    print(newstr)
                    print(i)
                    if newstr[i] == '[':
                            newstr[:-1]
                            i -=1
                    else:
                            return False
    if newstr == 'i':
        return True

bracesValid("(sup)how[you{doing}?](good?[good,{good[me?(I'm[great])]}])")