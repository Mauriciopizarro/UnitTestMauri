from app import maths


def test_sum():

	## arrange
	numX = 1
	numY = 2

	##act
	result = maths.sum(numX, numY)

	##assert
	assert result == 3



def test_sum_fail():

	## arrange
	numX = 2
	numY = 2

	##act
	result = maths.sum(numX, numY)

	##assert
	assert result != 5


