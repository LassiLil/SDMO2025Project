import unittest
from functions import containsNameAndInitial, process
print("testi")
'''
ANIRUDDHA ADAK   aniruddhaadak80@gmail.com,
Aniruddha Bhattacharjee    aniruddha97bhatt@gmail.com
0.6486486486486487,0.6451612903225806,1.0,0.23529411764705888,False,True,False,False
'''

'''
print(containsNameAndInitial("","",""))
print(containsNameAndInitial("etuliite","a","toinenNimi"))
print(containsNameAndInitial("aniruddha97bhatt","a","aniruddha"))
print(containsNameAndInitial("aaaa","b","aaaa"))
print(containsNameAndInitial("akuankka","a","ankka"))
'''

class TestContainsNameAndInitial(unittest.TestCase):

    def testEmpty(self):
        self.assertFalse(containsNameAndInitial("", "", "", ""))

    def testCorrect(self):
        self.assertTrue(containsNameAndInitial("firstlast", "f", "first", "last"))

    def testWrongInitial(self):
        self.assertFalse(containsNameAndInitial("firstlast", "g", "first", "last"))

    def testNumbersInPrefix(self):
        self.assertFalse(containsNameAndInitial("first12last", "f", "first", "last"))

    def testTreshold(self):
        self.assertFalse(containsNameAndInitial("firstlast", "f", "firzt", "last"))

class TestProcess(unittest.TestCase):

    def testEmptyName(self):
        self.assertEqual(process(("", "a@b")), ("", "", "", "", "", "a@b", "a", "b"))
    
    def testEmptyEmail(self):
        self.assertEqual(process(("first last", "")), ("first last", "first", "last", "f", "l", "", "", ""))
    
    def testCorrect(self):
        self.assertEqual(process(("first last", "a@b")), ("first last", "first", "last", "f", "l", "a@b", "a", "b"))

if __name__ == '__main__':
    unittest.main()

