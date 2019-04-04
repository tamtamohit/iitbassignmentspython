import sqlite3
import sys

class Employee:

    def __init__(self):
        mydb = sqlite3.connect('Employee_DB')
        self.c = mydb.cursor()
        self.file_path = sys.argv[1]
        # creating table
        try:
            self.c.execute('''CREATE TABLE Employee_Info (Name VARCHAR(20),ID INT,Salary INT,City VARCHAR(20))''')
        except:
            pass

    def read_csv_file(self):
        fo = open(self.file_path, 'r')
        # fo = open('employee_info.csv', 'r')
        data_csv = []
        for ln in fo.readlines():
            data_csv.append(ln.strip('\n').split(','))
        return data_csv

    def populate_table(self):
        data_csv = self.read_csv_file()
        for data in data_csv:
            x = '%s,%s,%s,%s'%(data[0], data[1], data[2], data[3])
            # self.c.execute('''insert into Employee_Info (John,1598,63000,Jaipur)''')#(data[0], int(data[1]), int(data[2]), data[3]))
            self.c.execute("INSERT INTO Employee_Info (Name,ID,Salary,City) VALUES (?,?,?,?)",(data[0], int(data[1]), int(data[2]), data[3]) )

    def print_all(self):
        for row in self.c.execute('''SELECT * FROM Employee_Info'''):
            print(row)

    def highest_salary(self):
        print('highest salary')
        for row in self.c.execute('''SELECT NAME,MAX(Salary) FROM Employee_Info'''):
            print(row[0],'has highest salary')
if __name__ == '__main__':
    ob = Employee()
    ob.populate_table()
    ob.print_all()
    ob.highest_salary()