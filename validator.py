import datetime
import re


class Validator:

    @staticmethod
    def validate_item(condition, item):
        validate = re.compile(condition)
        if re.fullmatch(validate, item):
            return True
        else:
            return False

    def validate_emp_id(self, emp_id):
        condition = '[A-Z][0-9]{3}'
        return self.validate_item(condition, emp_id)

    def validate_sales(self, sales):
        condition = '[0-9]{2,3}'
        return self.validate_item(condition, sales)

    def validate_salary(self, salary):
        condition = '[0-9]{2,3}'
        return self.validate_item(condition, salary)


    @staticmethod
    def validate_salary(salary):
        check = re.compile('[0-9]{2,3}')
        if re.fullmatch(check, salary):
            return True
        else:
            return False

    @staticmethod
    def validate_gender(gender):
        gender_values = ['F', 'M']
        tempt = gender
        if tempt in gender_values:
            return True
        else:
            return False

    # Chamilas
    @staticmethod
    def validate_bmi(bmi):
        bmi_values = ['Normal', 'Overweight', 'Underweight', 'Obesity']
        if bmi in bmi_values:
            return True
        else:
            return False



    # Jono's


    @staticmethod
    def validate_date(date_string):
        try:
            datetime.datetime.strptime(date_string, '%d-%m-%Y')
            return True
        except ValueError:
            return False

    @staticmethod
    def validate_age(age):
        check = re.compile('[0-9]{2}')
        if re.fullmatch(check, age):
            return True
        else:
            return False

    def validate_all(self, employee):
        if len(employee) >= 7:
            items_valid = [self.validate_emp_id(str(employee[0])),
                           self.validate_gender(str(employee[1])),
                           self.validate_age(str(employee[2])),
                           self.validate_sales(str(employee[3])),
                           self.validate_bmi(str(employee[4])),
                           self.validate_salary(str(employee[5])),
                           self.validate_date(str(employee[6]))]
        else:
            items_valid = {False, False, False, False, False, False, False}

        return items_valid

