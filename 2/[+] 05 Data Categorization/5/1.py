import pandas as pd

support = pd.read_csv(r'E:\courses\Data science\my\2\05 Data Categorization\2\support_log_grouped.csv')

def alert_group_importance(row):
    if row['alert_group'] == 'средний' and row['importance'] == 1:
        return('обратить внимание')
    
    elif row['alert_group'] == 'высокий' and row['importance'] == 1:
        return('высокий риск')
              
    elif row['alert_group'] == 'критичный' and row['importance'] == 1:
        return('блокер')

    else:
        return('в порядке очереди')

support_def = support.apply(alert_group_importance, axis=1)


support['importance_status'] = support.apply(alert_group_importance, axis=1)

print(support['importance_status'].value_counts())