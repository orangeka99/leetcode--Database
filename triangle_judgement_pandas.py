import pandas as pd
# Triangle Rules
def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    triangle['triangle'] = "Yes"
    triangle.loc[(abs(triangle['x']) + abs(triangle['y']) < abs(triangle['z'])), 'triangle'] = "No"
    triangle.loc[(abs(triangle['x']) + abs(triangle['z']) < abs(triangle['y'])), 'triangle'] = "No"
    triangle.loc[(abs(triangle['z']) + abs(triangle['y']) < abs(triangle['x'])), 'triangle'] = "No"
    triangle.loc[(abs(triangle['x']) + abs(triangle['z']) == abs(triangle['y'])), 'triangle'] = "No"
    triangle.loc[(abs(triangle['x']) + abs(triangle['y']) == abs(triangle['z'])), 'triangle'] = "No"
    triangle.loc[(abs(triangle['y']) + abs(triangle['z']) == abs(triangle['x'])), 'triangle'] = "No"
    return pd.DataFrame(triangle)