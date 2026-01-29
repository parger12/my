import pandas as pd

support = pd.read_csv(r'E:\courses\Data science\my\2\05 Data Categorization\2\support.csv')

support = support.rename(columns={
    'Тип обращения': 'type_message',
    'Время обращения': 'timestamp'
})

print (support)