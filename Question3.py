import os

import re


class Question3EmailAndMobile:
    def __init__(self,path_to_text_file):

        if os.path.isfile(path_to_text_file):
            self.path_to_text_file = path_to_text_file
        else:
            return print("Error: File not found, please give absolute path to the file.")

        self.start_searching()


    def start_searching(self):
        mobile_numbers = []
        emails = []
        words = []
        fo = open(self.path_to_text_file,'r')
        for line in fo.readlines():
            words = words + line.strip('\n').split(' ')

        for word in words:
            if self.mobile_number(word):
                mobile_numbers.append(word)
            elif self.email(word):
                emails.append(word)
        print(mobile_numbers)
        print(emails)

    def mobile_number(self, word):
        if word.isdigit() and len(word) == 10:
            return True
        else:
            return False

    def email(self, word):
        if bool(re.search('@',word)):
            email_split = word.split('@')
            if len(email_split) == 2:
                if bool(re.match("^[A-Za-z0-9_.]*$",email_split[0])):
                    email_sub_split = email_split[1].split('.')
                    if len(email_sub_split) == 2:
                        if bool(re.match("^[A-Za-z0-9]*$", email_sub_split[0])):
                            if bool(re.match("^[A-Za-z]*$", email_sub_split[1])):
                                return True
        return False

if __name__ == '__main__':
    ob = Question3EmailAndMobile('/home/mohit/Documents/test.txt')