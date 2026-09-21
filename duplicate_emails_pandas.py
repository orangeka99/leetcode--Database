import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    person = (
        person.sort_values('email')
        .assign(count_email=lambda df: df.groupby('email').cumcount() + 1)
        .query('count_email == 2')
    )
    return pd.DataFrame({'Email':person['email']})
