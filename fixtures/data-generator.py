##########################################################################
############################### Libraries ################################
##########################################################################

# SQL
from sqlalchemy import create_engine

# Others
import urllib
import numpy as np
import pandas as pd
from faker import Faker
from datetime import timedelta, datetime
from random import choice, randrange, sample, randint

##########################################################################
############################## Parameters ################################
##########################################################################

# SQL Sever Link
PASSWORD = "developer001password!"
USERNAME = "developer001"
URL_PATH = "localhost:1433"
DATABASE_NAME = "development"
connection_string = f"mssql+pyodbc://{USERNAME}:{PASSWORD}@{URL_PATH}/{DATABASE_NAME}?driver=ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=Yes"


# Role List 
role_list = [
    "CLEARK",
    "SALESMAN",
    "MANAGER",
    "PRESIDENT",
    "ANALYST"
]

# Department List
department_list = [
    "ACCOUNTING",
    "RESEARCH",
    "SALES",
    "OPERATIONS"
]

# Number of Employees
number_of_employees = 500

# Time Format
TIME_FORMAT = "%d-%b-%Y"

# Initial Date
initial_date = datetime.strptime('1/1/2008 1:30 PM', '%m/%d/%Y %I:%M %p')

##########################################################################
############################### Functions ################################
##########################################################################

def random_date(start, end):
    """
    CREDIT: https://stackoverflow.com/questions/553303/generate-a-random-date-between-two-other-dates
    This function will return a random datetime between two datetime 
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return datetime.strftime(start + timedelta(seconds=random_second), TIME_FORMAT)

def create_dept_dataframe(input_department_list):
    
    # Initialize Fake
    fake = Faker()
    
    # Assign Department Name and Location
    operating_dataframe = pd.DataFrame(
        data = {
            "DEPTNO": [(index+1) * 10 for index, _ in enumerate(input_department_list)],
            "DNAME": input_department_list,
            "LOC": [fake.address().split("\n")[1].split(",")[0] for _ in range(len(input_department_list))]
        }
    )
    
    return operating_dataframe

def create_employee_dataframe(input_number_of_employees, input_initial_date, input_role_list, input_department_dataframe):
    
    # Initialize Fake
    fake = Faker()
    
    operating_dataframe = pd.DataFrame(
        data = {
            "EMPNO": sample(range(1000, 5000), input_number_of_employees),
            "ENAME": [fake.unique.first_name() for _ in range(input_number_of_employees)],
            "JOB": [choice(input_role_list) for _ in range(input_number_of_employees)],
            "HIREDATE": [random_date(input_initial_date, datetime.now()) for _ in range(input_number_of_employees)],
            "SAL": [randint(1,100) * 100 for _ in range(input_number_of_employees)],
            "COMM": [randint(1,50) * 100 for _ in range(input_number_of_employees)],
            "DEPTNO":[choice(input_department_dataframe["DEPTNO"]) for _ in range(input_number_of_employees)],
        }
    )
    
    # Fix Commision
    operating_dataframe["COMM"] = operating_dataframe[["COMM", "JOB"]].apply(lambda x: np.nan if x["JOB"] != "SALESMAN" else x["COMM"], axis=1)
    
    # Create Manager
    operating_dataframe["MGR"] = [choice(operating_dataframe["EMPNO"]) for _ in range(input_number_of_employees)]
    
    # Remove PRESIDENT MANAGER
    operating_dataframe["MGR"] = operating_dataframe[["MGR", "JOB"]].apply(lambda x: x["MGR"] if x["JOB"] != "PRESIDENT" else np.nan, axis=1)
    
    return operating_dataframe

##########################################################################
################################# Main ###################################
##########################################################################

if __name__ == "__main__":
     
    # Create Department Dataframe
    department_dataframe = create_dept_dataframe(department_list)
   
    # Create Employee Dataframe
    employee_dataframe = create_employee_dataframe(
        number_of_employees,
        initial_date,
        role_list,
        department_dataframe
    )
    
    # Sanity Check:
    print(f"===== Department Dataframe =====\n{department_dataframe}\n===== Employee Dataframe =====\n{employee_dataframe}")

    # Inserting
    engine = create_engine(connection_string)
    
    # Insert the DataFrame into the SQL Server database
    # Replace 'your_table_name' with the actual table name you want to insert into
    department_dataframe.to_sql('dept', con=engine, if_exists='replace', index=False)
    employee_dataframe.to_sql('emp', con=engine, if_exists='replace', index=False)
    
    # Confirming
    for table_name in ['dept', 'emp']:
        sql_command = f'SELECT * FROM [{DATABASE_NAME}].[dbo].[{table_name}]'
        print(f"SQL command = {sql_command}")
        print(f"Output:\n{pd.read_sql_query(sql_command, con=engine)}")
        print("========================")
    
    # Close COnnection 
    engine.dispose()