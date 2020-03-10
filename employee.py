from peewee import *

try:
    db = PostgresqlDatabase('payrolSystem', user= 'postgres', host= 'localhost', password= '1234')
    print ('connection success')
except:
    print ('connection fail')

class Employee(Model):

    name = CharField('100')
    kra = CharField()
    houseallowance= FloatField()
    department = CharField()
    postion = CharField()
    basicsalary = FloatField()
    dob = DateField()

    class Meta:
        database = db #  This model uses the "payrollSystem.db" database.
        table_name_='employees'

Employee.create_table(fail_silently= True)
