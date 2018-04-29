import datetime
import re


class Validator:

    dic_condition = {'emp_id': '[A-Z][0-9]{3}','sales_salary': '[0-9]{2,3}'}

    def validate_item(self, item, regex):
        validate = re.compile(self.dic_condition[regex])
        if re.fullmatch(validate, item):
            return True
        else:
            return False


    def validate_age(self, age):
        condition = '[0-9]{2}'
        return self.validate_item(condition, age)

    @staticmethod
    def validate_data(values, item):
        if item in values:
            return True
        else:
            return False

    def validate_gender(self, gender):
        values = ['F', 'M']
        return self.validate_data(values, gender)

    def validate_bmi(self, bmi):
        values = ['Normal', 'Overweight', 'Underweight', 'Obesity']
        return self.validate_data(values, bmi)

    # Jono's
    @staticmethod
    def validate_date(date_string):
        try:
            datetime.datetime.strptime(date_string, '%d-%m-%Y')
            return True
        except ValueError:
            return False

    def validate_all(self, employee):
        if len(employee) >= 7:
            items_valid = [self.validate(str(employee[0]), 'emp_id'),
                           self.validate_gender(str(employee[1])),
                           self.validate_age(str(employee[2])),
                           self.validate_sales_salary(str(employee[3]), 'sales_salary'),
                           self.validate_bmi(str(employee[4])),
                           self.validate_sales_salary(str(employee[5]), 'sales_salary'),
                           self.validate_date(str(employee[6]))]
        else:
            items_valid = {False, False, False, False, False, False, False}

        return items_valid