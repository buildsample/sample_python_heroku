import unittest
from app import App

class TestSuite(unittest.TestCase):

    def test(self):
        app = App()
        app.calculate()
        self.failIf(app.retrieve() != 62)

def test1(self):
        app = App()
        app.calculate()
        self.failIf(app.retrieve() != 50)

def main():
    unittest.main()

if __name__ == "__main__":
    main()
