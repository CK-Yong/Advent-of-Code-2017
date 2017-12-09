import unittest
from CheckSumCalc import CheckSumCalc

class Test_ChecksumCalc(unittest.TestCase):
    def setUp(self):
        self.calc = CheckSumCalc()
        return super().setUp()

    def test_5195_should_return_8(self):
        # Act
        result = self.calc.GetDifference([5,1,9,5])
        # Assert
        self.assertEqual(result, 8)

    def test_753_should_return_4(self):
        # Act
        result = self.calc.GetDifference([7,5,3])
        # Assert
        self.assertEqual(result, 4)

    def test_2468_should_return_6(self):
        # Act
        result = self.calc.GetDifference([2,4,6,8])
        # Assert
        self.assertEqual(result, 6)    
        
    # Day 2
    def test_2468_should_return_6(self):
        # Act
        result = self.calc.GetDifferencesOfDivisions([5,9,2,8])
        # Assert
        self.assertEqual(result, 4)    
        
    def test_9473_should_return_3(self):
        # Act
        result = self.calc.GetDifferencesOfDivisions([9,4,7,3])
        # Assert
        self.assertEqual(result, 3)  
        
    def test_3865_should_return_3(self):
        # Act
        result = self.calc.GetDifferencesOfDivisions([3,8,6,5])
        # Assert
        self.assertEqual(result, 2)

    

if __name__ == '__main__':
    unittest.main()
