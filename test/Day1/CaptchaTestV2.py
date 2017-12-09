from Captcha import CaptchaV2
import unittest

class Test_CaptchaTestV2(unittest.TestCase):
    def setUp(self):
        self.captcha = CaptchaV2()
        return super().setUp()

    def test_It_should_return_6_from_1212(self):
        # Arrange 
        input = "1212"
		# Act
        result = self.captcha.Decode(input)
		# Assert
        self.assertEqual(result, 6)

    def test_It_should_return_0_from_1221(self):
        # Arrange
        input = "1221"
        # Act 
        result = self.captcha.Decode(input)
        # assert
        self.assertEqual(result,0)    
        
    def test_It_should_return_4_from_123425(self):
        # Arrange
        input = "123425"
        # Act 
        result = self.captcha.Decode(input)
        # assert
        self.assertEqual(result,4)    
        
    def test_It_should_return_12_from_123123(self):
        # Arrange
        input = "123123"
        # Act 
        result = self.captcha.Decode(input)
        # assert
        self.assertEqual(result, 12)   
        
    def test_It_should_return_4_from_12131415(self):
        # Arrange
        input = "12131415"
        # Act 
        result = self.captcha.Decode(input)
        # assert
        self.assertEqual(result, 4)
   
if __name__ == '__main__':
    unittest.main()
