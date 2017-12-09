from Captcha import Captcha
import unittest

class Test_CaptchaDecoding(unittest.TestCase):
	def setUp(self):
		self.captcha = Captcha()
		return super().setUp()
	
	def test_It_should_return_3_from_1122(self):
		# Arrange
		input = "1122"
		# Act
		result = self.captcha.Decode(input)
		# Assert
		self.assertEqual(result, 3)

	def test_It_should_return_4_from_1111(self):
		# Arrange
		input = "1111"
		# Act
		result = self.captcha.Decode(input)
		# Assert
		self.assertEqual(result, 4)

	def test_It_should_return_0_from_1234(self):
		# Arrange
		input = "0000"
		# Act
		result = self.captcha.Decode(input)
		# Assert
		self.assertEqual(result, 0)

	def test_It_should_return_9_from_91212129(self):
		# Arrange
		input = "91212129"
		# Act
		result = self.captcha.Decode(input)
		# Assert
		self.assertEqual(result, 9)

if __name__ == '__main__':
    unittest.main()