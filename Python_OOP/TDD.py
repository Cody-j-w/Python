import unittest

def reverseList(list):
    for x in range(0, (len(list))):
        if x==(len(list))/2:
            break
        list[x], list[-(x+1)] = list[-(x+1)], list[x]
    return list

class reverseListTests(unittest.TestCase):

    def testOne(self):
        self.assertEqual(reverseList([1,2,3]), [3,2,1])
    def testTwo(self):
        self.assertEqual(reverseList([5,2,7,1]), [1,7,2,5])
    def testThree(self):
        self.assertEqual(reverseList([3,3,3,3,3]), [3,3,3,3,3])
    def setUp(self):
        print("running setUp")
    def tearDown(self):
        print("running tearDOwn tasks")

if __name__ == '__main__':
    unittest.main()




# def palindromeFinder(string):
#     control = string
#     result = " "
#     for x in((len(string)),-1,-1):
#         result += string[x]
#     if control == result:
#         return True
#     else:
#         return False

# def coins()