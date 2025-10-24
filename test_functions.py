import unittest
from functions import contains_name_and_initial, process, check_c2

class Test_contains_name_and_initial(unittest.TestCase):

    def testEmpty(self):
        self.assertFalse(contains_name_and_initial("", "", "", ""))

    def testCorrect(self):
        self.assertTrue(contains_name_and_initial("firstlast", "f", "first", "last"))

    def testWrongInitial(self):
        self.assertFalse(contains_name_and_initial("firstlast", "g", "first", "last"))

    def testNumbersInPrefix(self):
        self.assertFalse(contains_name_and_initial("first12last", "f", "first", "last"))

    def testTreshold(self):
        self.assertFalse(contains_name_and_initial("firstlast", "f", "firzt", "last"))

class Test_process(unittest.TestCase):

    def testEmptyName(self):
        self.assertEqual(process(("", "a@b")), ("", "", "", "", "", "a@b", "a", "b"))
    
    def testEmptyEmail(self):
        self.assertEqual(process(("first last", "")), ("first last", "first", "last", "f", "l", "", "", ""))
    
    def testCorrect(self):
        self.assertEqual(process(("first last", "a@b")), ("first last", "first", "last", "f", "l", "a@b", "a", "b"))

    def testEmptyDomain(self):
        self.assertEqual(process(("first last", "a")), ("first last", "first", "last", "f", "l", "a", "a", ""))

    def testEmptyPrefix(self):
        self.assertEqual(process(("first last", "@b")), ("first last", "first", "last", "f", "l", "@b", "", "b"))

#Chris Sternal-Johnson,chris@sternal-johnson.com,Chris Wiederspan,chris@wiederspan.com
    class test_check_c2(unittest.TestCase):

        def testCorrect(self):
            self.assertTrue(check_c2("prefix", "prefix", "first", "first", "last", "last"))

        def testWrongLastName(self):
            self.assertFalse(check_c2("prefix", "prefix", "first", "first", "last", "different"))

        def testWrongFirstName(self):
            self.assertFalse(check_c2("prefix", "prefix", "first", "different", "last", "last"))

        def testWrongPrefixName(self):
            self.assertFalse(check_c2("prefix", "different", "first", "first", "last", "last"))

if __name__ == '__main__':
    unittest.main()

