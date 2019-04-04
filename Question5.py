import sys
import argparse
import csv

import os


class Question5StudentDatabase:
    def __init__(self):
        self.csvfile = '/home/mohit/Documents/test.csv'
        if not os.path.isdir(os.path.split(self.csvfile)[0]):
            return print("Error: Invalid folder name. Folder not found please check file path in line 10. Folder names are case sensitive, please check the folder name.")

        parser = argparse.ArgumentParser()
        parser.add_argument("--first_name", help="First name of student.")
        parser.add_argument("--last_name", help="Last name of student.")
        parser.add_argument("--roll_no", help="Roll number of student.")
        parser.add_argument("--gender", help="Gender.")
        parser.add_argument("--mobile", help="Personal Contact Number.")
        parser.add_argument("--dept", help="Department.")
        parser.add_argument("--CGPA", help="CGPA.")

        required_items = []
        self.args = parser.parse_args()
        for k, v in self.args.__dict__.items():
            if v == None:
                required_items.append(k)

        if len(required_items) > 0:
            return print('the following arguments are required: --' + ', --'.join(required_items))

        self.check_file()
        self.append_data()

    def mobile_number(self):
        if self.args.mobile.isdigit() and len(self.args.mobile) == 10:
            return True
        else:
            print('Error: Insignificant mobile number.')
            return False

    def roll_no(self):
        if self.args.roll_no.isdigit():
            return True
        else:
            print('Error: Roll no must be an integer.')
            return False


    def CGPA(self):
        try:
            float(self.args.CGPA)
            return True
        except ValueError:
            'Error: Please enter a float type CGPA.'
            return False

    def check_file(self):
        if os.path.isfile(self.csvfile):
            return
        else:
            fo = open(self.csvfile, 'w+')
            fo.write("First Name,Last Name,Roll Number,Gender,Mobile,Dept,CGPA\n")
            fo.close()

    def append_data(self):
        if not self.mobile_number(): return
        if not self.CGPA(): return
        if not self.roll_no(): return
        fo = open(self.csvfile, 'a+')
        fo.write(','.join(
            [self.args.first_name, self.args.last_name, self.args.roll_no, self.args.gender, self.args.mobile,
             self.args.dept, self.args.CGPA]) + '\n')
        fo.close()


if __name__ == '__main__':
    ob = Question5StudentDatabase()
