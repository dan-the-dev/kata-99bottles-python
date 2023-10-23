import unittest
import Song99Bottles as Song99BottlesClass

class Song99BottlesTest(unittest.TestCase):
    main = Song99BottlesClass.Song99Bottles()  # instantiate the Person Class

    # test case function to check the Person.set_name function
    def test_shall_pass(self):
        self.assertTrue(self.main.handle())
