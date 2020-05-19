import unittest
from test import TestMath

def suite():

	test_suite = unittest.TestSuite()
	test_suite.addTest(unittest.makeSuite(TestMath))
	return test_suite

if __name__ == "__main__" :

	alltests = unittest.TestSuite() 
	alltests.addTest(suite())
	unittest.TextTestRunner().run(alltests)

	

