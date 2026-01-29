import pandas as pd

support = pd.read_csv(r'E:\courses\Data science\my\2\05 Data Categorization\2\support.csv')

support = support.rename(columns={
    'Тип обращения': 'type_message',
    'Время обращения': 'timestamp'
})

support_log = support[['user_id', 'type_id', 'timestamp']]

support_dict = support[['type_message', 'type_id']]

support_dict = support_dict.drop_duplicates().reset_index(drop=True)


print (support_dict.sort_values('type_id', ascending=True))