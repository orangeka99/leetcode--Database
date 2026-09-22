import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    employee['max_salary'] = employee.groupby('departmentId')['salary'].transform('max')
    employee = employee[employee['salary'] == employee['max_salary']]
    employee = pd.merge(employee, department, left_on='departmentId', right_on='id', how='inner')    
    return pd.DataFrame({'Department':employee['name_y'],
                         'Employee':employee['name_x'],
                         'Salary':employee['salary']})