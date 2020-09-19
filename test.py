import unittest 
import maths  

class TestMath(unittest.TestCase):
	
	def test_sum(self):

		## arrange
		numX = 1
		numY = 2

		##act
		result = maths.sum(numX,numY)

		##assert 
		self.assertEqual(result,3)




