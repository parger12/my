import pandas as pd
board_df = pd.read_csv(r'E:\courses\Data science\my\1\Basic Python\09 the pandas library\game_board.csv')

print (board_df[board_df['H'] == 1]['H'])