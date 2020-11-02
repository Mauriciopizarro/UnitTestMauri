from app import maths


def test_sum():

	## arrange
	numX = 1
	numY = 2

	##act
	result = maths.sum(numX, numY)

	##assert
	assert result == 3





