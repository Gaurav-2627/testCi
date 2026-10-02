import unittest
from main import to_upper 

class testvala(unittest.TestCase):
    def test_check(self):
        name = "Gaurav"
        res = to_upper(name)
        self.assertEqual(res,"GAURAV")

if __name__ == "__main__":
    unittest.main()
