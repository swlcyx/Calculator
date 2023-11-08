import unittest


class MyTestCase(unittest.TestCase):
    def equalall(self,string):
        string = string.replace('%', '/100').replace('x', '*')
        try:
            num = round(eval(string), 8)
            return num
        except:
            num = 'Wrong Expression!'
            return num

    def test_equal(self):
        self.assertEqual(self.equalall("1+1"), 2)
        self.assertEqual(self.equalall("1x2"), 2)
        self.assertEqual(self.equalall("1/0"), 'Wrong Expression!')
        self.assertEqual(self.equalall("1+-x/2"), 'Wrong Expression!')


if __name__ == '__main__':
    unittest.main()
