import pandas as pd

PATHTOPLAYS = 'PATH TO plays.csv HERE'
PATHTOPASSPLAYS = 'OUTPUT PATH TO pass_plays.csv HERE'

plays_df = pd.read_csv(PATHTOPLAYS)
passes = plays_df[(plays_df['PassResult'] == 'C') | (plays_df['PassResult'] == 'I') | (plays_df['PassResult'] == 'IN') | (plays_df['PassResult'] == 'S')] 
passes.to_csv(PATHTOPASSPLAYS)