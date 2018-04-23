import unittest
from validator import Validator


class ValidatorUnitTest(unittest.TestCase):
    def test_validate_emp_id_is_true(self):
        v = Validator()
        result = v.validate_emp_id("A002")
        self.assertTrue(result, 'valid employee id')

    def test_validate_emp_id_too_long_is_false(self):
        v = Validator()
        result = v.validate_emp_id("A0001")
        self.assertFalse(result, 'invalid employee id')

    def test_validate_emp_id_num_only_is_false(self):
        v = Validator()
        result = v.validate_emp_id("0001")
        self.assertFalse(result, 'valid employee id')

    def test_validate_emp_id_no_num_is_false(self):
        v = Validator()
        result = v.validate_emp_id("AAAA")
        self.assertFalse(result, 'invalid employee id')

    def test_validate_emp_id_low_case_is_false(self):
        v = Validator()
        result = v.validate_emp_id("a001")
        self.assertFalse(result, 'invalid employee id')

    def test_validate_emp_id_is_false(self):
        v = Validator()
        result = v.validate_emp_id("A02")
        self.assertFalse(result, 'invalid employee id')

    def test_validate_gender_is_true(self):
        """
        Test the validate gender function
        """
        result = Validator.validate_gender("F")
        self.assertTrue(result, 'valid GENDER')

    def test_validate_gender_with_lowcase_is_false(self):
        """
        Test the validate gender function
        """
        result = Validator.validate_gender("f")
        self.assertFalse(result, 'valid GENDER')

    def test_validate_gender_with_long_input_is_true(self):
        """
        Test the validate gender function
        """
        result = Validator.validate_gender("Female")
        self.assertFalse(result, 'invalid GENDER')

    def test_validate_gender_with_upper_only_is_False(self):
        """
        Test the validate gender function
        """
        result = Validator.validate_gender("FEMALE")
        self.assertFalse(result, 'valid GENDER')

    def test_validate_gender_is_false(self):
        """
        Test the validate gender function
        """
        result = Validator.validate_gender("E")
        self.assertFalse(result, 'invalid GENDER')
    def test_validate_salary_is_true(self):
        """
        Test the validate salary function
        :return: True
        """
        v = Validator()
        result = v.validate_salary("20")
        self.assertTrue(result, 'valid Salary')

        def test_validate_salary_is_true_3_digit(self):
            """
            Test the validate salary function
            :return: True
            """
            v = Validator()
            result = v.validate_salary("200")
            self.assertTrue(result, 'valid Salary')

    def test_validate_salary_is_false_words(self):
        """
        Test the validate salary function
        :return: True
        """
        v = Validator()
        result = v.validate_salary("seventy thousand")
        self.assertFalse(result, 'valid Salary')

    def test_validate_salary_is_false_negative_value(self):
        """
        Test the validate salary function
        :return: True
        """
        v = Validator()
        result = v.validate_salary("-20")
        self.assertFalse(result, 'invalid Salary')

    def test_validate_salary_is_false_too_big(self):
        """
        Test the validate salary function
        :return:
        """
        v = Validator()
        result = v.validate_salary('8000')
        self.assertFalse(result, 'invalid SALARY')

    def test_validate_salary_is_false_too_small(self):
        """
        Test the validate salary function
        :return:
        """
        v = Validator()
        result = v.validate_salary('8')
        self.assertFalse(result, 'invalid SALARY')

    def test_validate_salary_is_true_small_but_includes_zero(self):
        """
        Test the validate salary function
        :return:
        """
        v = Validator()
        result = v.validate_salary('008')
        self.assertTrue(result, 'valid SALARY')

    def test_validate_date_is_true(self):
        """
        Test the validate date function
        :return: True
        """
        v = Validator()
        result = v.validate_date("02-03-1990")
        self.assertTrue(result, 'valid Date')

    def test_validate_date_is_false_words(self):
        """
        Test the validate date function
        :return: True
        """
        v = Validator()
        result = v.validate_date("02-March-1991")
        self.assertFalse(result, 'invalid Date format')

    def test_validate_date_is_false_invalid_format(self):
        """
        Test the validate date function
        :return:
        """
        v = Validator()
        result = v.validate_date('01/08/1991')
        self.assertFalse(result, 'invalid date, wrong format')

    def test_validate_date_is_false_invalid_date(self):
        """
        Test the validate date function
        :return:
        """
        v = Validator()
        result = v.validate_date('89/13/1991')
        self.assertFalse(result, 'invalid date, date doesnt exist')

    def test_validate_age_is_true(self):
        """
        Test the validate age function
        :return: True
        """
        v = Validator()
        result = v.validate_age("20")
        self.assertTrue(result, 'valid AGE')

    def test_validate_age_is_false(self):
        """
        Test the validate age function
        :return:
        """
        v = Validator()
        result = v.validate_age('8000')
        self.assertFalse(result, 'invalid AGE')

    def test_validate_age_is_false_negative_num(self):
        """
        Test the validate age function
        :return:
        """
        v = Validator()
        result = v.validate_age('-20')
        self.assertFalse(result, 'invalid AGE')

    def test_validate_all_all_true(self):
        """
        Test valid data being passed into validate_all
        :return:
        """
        v = Validator()
        list1 = ['A001', 'M', '26', '200', 'Normal', '20', '08-10-1991']
        result = v.validate_all(list1)
        expected = [True, True, True, True, True, True, True]
        self.assertEqual(expected, result, "Not valid input")

    def test_validate_all_with_false(self):
        """
        Test invalid date being passed through and if list recognises it
        :return:
        """
        v = Validator()
        list1 = ['A001', 'M', '26', '200', 'Normal', '20', '08/10/1991']
        result = v.validate_all(list1)
        expected = [True, True, True, True, True, True, False]
        self.assertEqual(expected, result, "invalid input")
    def test_validate_bmi_is_true(self):
        v = Validator()
        result = v.validate_bmi("Normal")
        self.assertTrue(result, "Valid BMI")

    def test_validate_bmi_is_false(self):
        v = Validator()
        result = v.validate_bmi("normal")
        self.assertFalse(result, "Invalid BMI")

    def test_validate_sales_is_true(self):
        v = Validator()
        result = v.validate_sales("999")
        self.assertTrue(result, 'Valid Sales value')

    def test__validate_sales_is_false(self):
        v = Validator()
        result = v.validate_sales("1234")
        self.assertFalse(result, 'Invalid Sales Amount')

    def test_15_validate_bmi_is_false_notequal_under(self):
        """
        Test the validate bmi true function
        :return:
        """
        v = Validator()
        result = v.validate_bmi("U")
        self.assertNotEqual(result, 'Underweight', "Invaid BMI")

    def test_14_validate_bmi_is_false_notequal_over(self):
        """
        Test the validate bmi true function
        :return:
        """
        v = Validator()
        result = v.validate_bmi("OVERWEIGHT")
        self.assertNotEqual(result, 'Overweight', "Invaid BMI")

    def test_13_validate_bmi_is_false_notequal_normal(self):
        """
        Test the validate bmi true function
        :return:
        """
        v = Validator()
        result = v.validate_bmi("NORMAL")
        self.assertNotEqual(result, 'Normal', "Invaid BMI")

    def test_12_validate_bmi_is_false_notEqualO(self):
        """
        Test the validate bmi true function
        :return:
        """
        v = Validator()
        result = v.validate_bmi("OBESITY")
        self.assertNotEqual(result, 'Obesity', "Invaid BMI")

    def test_11_validate_bmi_is_false_notEqualN(self):
        """
        Test the validate bmi true function
        :return:
        """
        v = Validator()
        result = v.validate_bmi("N")
        self.assertNotEqual(result, 'Normal', "Invaid BMI")

    def test_10_validate_bmi_is_false_space(self):
        """
        Test the validate bmi true function
        :return:
        """
        v = Validator()
        result = v.validate_bmi("  ")
        self.assertFalse(result, "Invalid BMI")

    def test_09_validate_bmi_is_true(self):
        """
        Test the validate bmi true function
        :return:
        """
        v = Validator()
        result = v.validate_bmi("Normal")
        self.assertTrue(result, "Valide BMI")

    def test_08_validate_bmi_is_false(self):
        """
        Test the validate bmi false function
        :return:
        """
        v = Validator()
        result = v.validate_bmi("normal")
        self.assertFalse(result, "Invalide BMI")

    def test_07_validate_bmi_is_false_N(self):
        """
        Test the validate bmi false function
        :return:
        """
        v = Validator()
        result = v.validate_bmi("N")
        self.assertFalse(result, "Invalide BMI")

    def test_06_validate_sales_is_true(self):
        """
        Test the validate sales true function
        :return:
        """
        v = Validator()
        result = v.validate_sales("999")
        self.assertTrue(result, 'Valide Sales value')

    def test_05_validate_sales_is_false(self):
        """
        Test the validate sales false function
        :return:
        """
        v = Validator()
        result = v.validate_sales("1234")
        self.assertFalse(result, 'Invalide Sales Amount')

    def test_04_validate_sales_is_false_space(self):
        """
        Test the validate sales false function
        :return:
        """
        v = Validator()
        result = v.validate_sales(" ")
        self.assertFalse(result, 'Invalide Sales Amount')

    def test_03_validate_sales_is_false_characters(self):
        """
        Test the validate sales false function
        :return:
        """
        v = Validator()
        result = v.validate_sales(",")
        self.assertFalse(result, 'Invalide Sales character')

    def test_02_validate_sales_is_false_letters(self):
        """
        Test the validate sales false function
        :return:
        """
        v = Validator()
        result = v.validate_sales("qwer")
        self.assertFalse(result, 'Invalide Sales you can not enter letters')

    def test_01_validate_sales_is_false_minus(self):
        """
        Test the validate sales false function
        :return:
        """
        v = Validator()
        result = v.validate_sales("-3")
        self.assertFalse(result, 'Invalid Sales you cant enter minus values')
