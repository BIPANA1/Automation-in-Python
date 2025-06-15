import unittest


class MyTestCase(unittest.TestCase): #function method, class

    @classmethod
    def setUpClass(cls):
        print("I'm SetUp")

    @classmethod
    def tearDownClass(cls):
        print("I am tearDown")

    def test_b(self):
        print("I ran from b")  # add assertion here
        self.assertEqual(True,True,"Both are not same")
        self.assertNotEqual(True,False,"Both are same")


    #naming convention which comes alphabhet 1st
    def test_a(self):
        print("I ran from a")

# for automating login multiple pages we use function method
# register class method

if __name__ == '__main__':
    unittest.main()
