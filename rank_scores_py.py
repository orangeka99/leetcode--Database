import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores = scores.assign(rank=scores['score'].rank(method='dense', ascending=False).astype(int)
    ).sort_values(by='score', ascending=False)
    return pd.DataFrame({'score': scores['score'],
                         'rank' : scores['rank']})