import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    courses['r1'] = courses.groupby('class')['class'].transform('count')
    courses = courses[courses['r1'] >= 5]
    courses = courses['class'].unique()
    return pd.DataFrame({'class':courses})