import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    unique_salaries = employee['salary'].drop_duplicates().sort_values(ascending=False)
    
    if N > 0 and N <= len(unique_salaries):
        result = unique_salaries.iloc[N - 1]
    else:
        result = None

    column_name = f"getNthHighestSalary({N})"
    return pd.DataFrame({column_name: [result]})