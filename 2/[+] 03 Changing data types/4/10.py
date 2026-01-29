import pandas as pd
data = pd.read_excel(r'E:\courses\Data science\my\2\03 Changing data types\2\seo_data.xlsx', sheet_name='traffic_data') 
data ['visits'] = pd.to_numeric(data['visits'], errors='coerce')
print(data[data['subcategory_id'] == 'total'])