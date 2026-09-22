import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    person.sort_values(by='id',inplace=True)
    person.drop_duplicates('email', keep='first', inplace=True)


