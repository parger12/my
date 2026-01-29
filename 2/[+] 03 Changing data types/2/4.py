import pandas as pd
data = pd.read_excel(r'E:\courses\Data science\my\2\03 Changing data types\2\seo_data.xlsx', sheet_name='traffic_data') 
subcategory_dict =pd.read_excel (r'E:\courses\Data science\my\2\03 Changing data types\2\seo_data.xlsx', sheet_name='subcategory_ids') 
category_dict = pd.read_excel (r'E:\courses\Data science\my\2\03 Changing data types\2\seo_data.xlsx', sheet_name='category_ids') 
print (category_dict.head)