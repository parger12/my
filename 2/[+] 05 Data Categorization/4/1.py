import pandas as pd

support = pd.read_csv(r'E:\courses\Data science\my\2\05 Data Categorization\2\support_log.csv')

support_log_grouped = support.groupby('type_id').count()

def alert_group(messages):
    if messages <= 300:
        return ('средний')
    if 301 <= messages <= 500:
        return ('высокий')
    else:
        return ('критичный')
    
support_log_grouped['alert_group'] = support_log_grouped['user_id'].apply(alert_group)

print(support_log_grouped.groupby('alert_group')['alert_group'].count())