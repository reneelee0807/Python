import unittest
from filer import Filer


class FilerUnitTest(unittest.TestCase):

    def test_read_file_from_csv(self):
        f = Filer()
        result = f.read_csv("test_renee.csv")
        expected = [['EMPID', 'GENDER', 'AGE', 'SALES', 'BMI',
                     'SALARY', 'BIRTHDAY'],
                    ['A001', 'M', '26', '200', 'Normal', '20', '08-10-1991'],
                    ['A002', 'F', '26', '300', 'Normal', '30', '09-10-1991']]
        self.assertEqual(expected, result, "didnt read file correctly")

    def test_read_not_found_csv_exception(self):
        f = Filer()
        with self.assertRaises(FileNotFoundError) as context:
            f.read_csv('unfound.csv')
            self.assertTrue('No such file or directory')
            # self.assertRaises(FileNotFoundError, f.read_csv('unfound.csv'))

    def test_os_error_read_csv_exception(self):
        f = Filer()
        self.assertRaises(TypeError, f.read_csv('test2.db'))

    def test_can_not_open_csv_general_exception(self):
        f = Filer()
        self.assertRaises(Exception, f.read_csv('test'))

    def test_name_error_save_cvs_exception(self):
        f = Filer()
        self.assertRaises(NameError, f.save_csv('#####.csv', [1, 2, 3]))

    def test_can_not_save_csv_file_exist_error_exception(self):
        f = Filer()
        ans = f.save_csv('test_renee.csv', [1, 2, 3])
        self.assertRaises(FileExistsError, ans)

    def test_can_not_save_csv_general_exception(self):
        f = Filer()
        self.assertRaises(Exception, f.save_csv('test', [1, 2, 3]))

    # Jonno's
    def test_filer_read_excel(self):
        """
        Test if it can read an xlsx document
        :return: list
        """
        f = Filer()
        result = f.read_excel("test.xlsx")
        expected = [['A001', 'M', 26, 200, 'Normal', 20, '08-10-1991'],
                    ['A002', 'F', 26, 300, 'Normal', 30, '09-10-1991']]
        self.assertEqual(result, expected, "file does not match")

    def test_filer_save_excel_and_read_saved(self):
        """
        Test if it can save to excel
        :return:
        """
        f = Filer()
        li1 = [['A001', 'M', '26', '200', 'Normal', '20', '08-10-1991'],
               ['A002', 'F', '26', '300', 'Normal', '30', '09-10-1991']]
        f.save_excel('doc_test22.xlsx', li1)
        result = f.read_excel("doc_test22.xlsx")
        expected = [['A002', 'F', 26, 300, 'Normal', 30, '09-10-1991']]
        self.assertEqual(result, expected, "saved file couldn't be read")