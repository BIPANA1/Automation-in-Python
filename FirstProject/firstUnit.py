import unittest


class MyTestCase(unittest.TestCase): #function method, class
    # tests before test, test and after test
    # this is function method
    def setUp(self):
        print("I'm SetUp")

    def tearDown(self):
        print("I'm TearDown")

    def test_b(self):
        print("I ran from b")  # add assertion here


    #naming convention which comes alphabhet 1st
    def test_a(self):
        print("I ran from a")


if __name__ == '__main__':
    unittest.main()
