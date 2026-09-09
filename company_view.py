import mysql.connector
from datetime import datetime


class ConnectdB:
    def get_connection(self):
        try:
            self.connection=mysql.connector.connect(
                host="localhost",
                user="root",
                password="alanr.ec2226",
                database="companydb"
            )
            return self.connection
        except Exception as e:
            return None

class EmployeeManager(ConnectdB):
    def post(self,**kwargs):
        try:
            self.connect=super().get_connection()
            self.cursor=self.connect.cursor()
            query="insert into employee (name,place,mobile,email,department,salary,joining_date) values (%s,%s,%s,%s,%s,%s,%s)"
            values=[v for v in kwargs.values()]
            self.cursor.execute(query,values)
            self.connect.commit()
            print("Employee Added Successfully.")
        except Exception as e:
            print(e)

    def get(self):
        try:
            self.connect=super().get_connection()
            self.cursor=self.connect.cursor()
            query="select * from employee"
            self.cursor.execute(query)
            record=self.cursor.fetchall()
            print(record)
        except Exception as e:
            print(e)

    def get_object(self,id=None):
        try:
            self.connect=super().get_connection()
            self.cursor=self.connect.cursor()
            query="select * from employee id where id=%s"
            values=(id,)
            self.cursor.execute(query,values)
            record=self.cursor.fetchone()
            return record
        except Exception as e:
            return None


    def put(self,id=None,**kwargs):
        try:
            record=self.get_object(id=id)
            if record!=None:
                placeholder=""
                for k in kwargs.keys():
                    placeholder+=k+"=%s,"
                placeholder=placeholder.rstrip(",")
                query=f"update employee set {placeholder} where id=%s"
                values=[v for v in kwargs.values()]
                values.append(id)
                self.cursor.execute(query,values)
                self.connect.commit()
                print("Employee updated successfully")
            else:
                print("Employee not found")
        except Exception as e:
            print(e)

    def delete(self,id=None):
        try:
            record=self.get_object(id=id)
            values=(id,)
            if record!=None:
                query="delete from employee where id=%s"
                self.cursor.execute(query,values)
                self.connect.commit()
                print("Employee deleted successfully")
            else:
                print("employee not found")
        except Exception as e:
            print(e)

    def retrieve(self,id=None):
        try:
            record=self.get_object(id=id)
            if record==None:
                print("Employee not found")
            else:
                print(record)
        except Exception as e:
            print(e)

employee_instance=EmployeeManager()
# employee_instance.post(name="shyam",place="kakanadu",mobile="83767187367",email="shyam@yahoo.com",department="IT",salary=25000,joining_date=datetime.today())
# employee_instance.get()
# employee_instance.put(id=3,email="shyam@gmail.com",salary=50000)
# employee_instance.delete(1)
# employee_instance.retrieve(2)
employee_instance.get()