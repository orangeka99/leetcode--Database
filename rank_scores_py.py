import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    def_sort = scores['score'].sort_values(ascending=False)
    prev_val = 0.00
    my_dict = {'score':[],
                'rank':[]
                }
    rank_id = 1
    for i1 in range(len(def_sort)):
        if i1 == 0:
            prev_val = def_sort.iloc[i1]
            my_dict.setdefault('score',[]).append(prev_val)
            my_dict.setdefault('rank',[]).append(rank_id)
        else:
            if def_sort.iloc[i1] != prev_val:
                rank_id += 1
                prev_val = def_sort.iloc[i1]
            my_dict.setdefault('score',[]).append(prev_val)
            my_dict.setdefault('rank',[]).append(rank_id)

    return pd.DataFrame(my_dict)