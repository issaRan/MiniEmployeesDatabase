import sqlite3


class ManageDb:
    def __init__(self):
        self.db = sqlite3.connect('employess.db')
        c = self.db.cursor()
        c.execute('''CREATE TABLE if not exists emp(id integer primary key AUTOINCREMENT,
        name text, email text, phone_num text, type text, experience integer, salary text)''')
        self.db.commit()

    def saveToDataBase(self, employee):
        self.db.execute(
            "insert into emp(name,email,mobile_no,type,experience,salary) values(:name,:email,:mobile_no,:type,:experience,:salary)",
            {'name': employee._empName, 'email': employee._empEmail, 'mobile_no': employee._mobile,
             'type': employee._empType, 'experience': employee._experience,
             'salary': employee._slaray})
        self.db.commit()

    def display(self):
        eid = input("enter the emp id: ")
        with self.con:
            dataEmp = self.con.execute(
                'select id,name,email,mobile_no,type,experience,salary from emp where id=:id',
                {'id': eid})
            data = dataEmp.fetchall()
            print("Name : " + data[0][1])
            print("Email : " + data[0][2])
            print("Mobile No. : " + data[0][3])
            print("Employee Type : " + data[0][4])
            print("Experience : ", data[0][5])
            print("Salary : ", data[0][6])

    def delete_task(self):
        eid = input("enter the emp id: ")
        sql = 'DELETE FROM tasks WHERE id=:eid'
        cur = self.db.cursor()
        cur.execute(sql, (eid,))
        self.db.commit().con.commit()
