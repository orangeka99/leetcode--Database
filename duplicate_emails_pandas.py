import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    person = person.sort_values(by='email', ascending=True)
    person['count_email'] = person.groupby('email').cumcount() + 1
    person = person[person['count_email'] == 2]
    return pd.DataFrame({'Email':person['email']})
