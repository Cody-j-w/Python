x[1][0] = 15

students[0]['last_name'] ='Bryant'

sports_directory['soccer'][0] = 'Andres'

z[0]['y'] = 30

def iterateDictionary(students):
    for x in range(0, (len(list))):
        print('first_name', ' - ', students[x]['first_name'], ', ', 'last_name', ' - ', students[x]['last_name'])

def iterateDictionary2(students):
    for x in range(0, (len(list))):
        print(students[x]['first_name'])


def printDojoInfo(dojo):
    print(1+(len(dojo['location'])),'LOCATIONS')
    for x in range(0,(len(dojo['location']))):
        print(dojo['location'][x])
    print(1+(len(dojo['instructors'])), 'INSTRUCTORS')
    for i in range(0,(len(dojo['instructors']))):
        print(dojo['instructors'][i])
        



