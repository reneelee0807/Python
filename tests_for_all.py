import doctest


def doc_tests():
    doctest.testfile("test/doc_test_filer.txt", verbose=1)


if __name__ == "__main__":
    doc_tests()
    # runner = unittest.TextTestRunner(verbosity=2)
    #
    # test_suite = unit_tests()
    # runner.run(test_suite)