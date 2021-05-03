
import pandas as pd

df = pd.read_excel(r'D:\IPL-PLAYERS.xlsx')
#print(df)

import random
#players = df[['CODE']]
#print(players)
#player = sorted(players)
list_code = df['SERIAL'].to_list()
print(list_code)
list_name = df['PLAYER NAMES'].to_list()
list0 = {list_code[i]: list_name[i] for i in range(len(list_code))}
print(list0)
# player_sorted = list_name[1:25]
# list1 = random.sample(list0 , 11)
# captain = random.sample(list1, 2)
# #print(captain)
# team1 = captain+list1
# print(team1)


a = df[['SERIAL']]
print(a)

















