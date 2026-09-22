import pandas as pd

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    employee = pd.merge(employee, department, left_on='departmentId', right_on='id',how='inner')
    employee['gg'] = employee.groupby('departmentId')['salary'].rank(method='dense', ascending=False)
    employee = employee[employee['gg'] <= 3]
    return pd.DataFrame({'Department':employee['name_y'],
                         'Employee':employee['name_x'],
                         'Salary':employee['salary']})
    