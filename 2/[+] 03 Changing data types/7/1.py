import pandas as pd
data = pd.read_excel(r'E:\courses\Data science\my\2\03 Changing data types\7\seo_data.xlsx', sheet_name='traffic_data')
subcategory_dict = pd.read_excel(r'E:\courses\Data science\my\2\03 Changing data types\7\seo_data.xlsx', sheet_name='subcategory_ids')
data_subcategory = data.merge(subcategory_dict, on='subcategory_id', how='left')
print (data_subcategory)