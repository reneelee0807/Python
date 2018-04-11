from test.unit_test_filer import FilerUnitTest
from test.unit_test_validator import ValidatorUnitTest
from test.unit_test_employee import EmployeeUnitTest
from test.unit_test_controller import ControllerUnitTest
from test.unit_test_database import DatabaseUnitTest

import doctest
import unittest


def doc_tests():
    doctest.testfile("test/doc_test_filer.txt", verbose=1)
    doctest.testfile("test/doc_test_validator.txt", verbose=1)


def unit_tests():
    the_suite = unittest.TestSuite()

    the_suite.addTest(unittest.makeSuite(FilerUnitTest))
    the_suite.addTest(unittest.makeSuite(ValidatorUnitTest))
    the_suite.addTest(unittest.makeSuite(EmployeeUnitTest))
    the_suite.addTest(unittest.makeSuite(ControllerUnitTest))
    the_suite.addTest(unittest.makeSuite(DatabaseUnitTest))

    return the_suite


if __name__ == "__main__":
    doc_tests()
    runner = unittest.TextTestRunner(verbosity=2)

    test_suite = unit_tests()
    runner.run(test_suite)