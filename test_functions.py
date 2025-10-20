import unittest
from functions import containsNameAndInitial, process

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

