
financial_info = {
    'American Express': 93.23,
    'Boeing': 178.44,
    'Coca-Cola': 45.15,
    'Nike': 97.99,
    'JPMorgan':96.27,
    'Walmart': 130.68,
    'Walt Disney': 119.34
}

walmart_price = financial_info ['Walmart']
print(walmart_price)


financial_info = {
    'American Express': 93.23,
    'Boeing': 178.44,
    'Coca-Cola': 45.15,
    'Nike': 97.99,
    'JPMorgan':96.27,
    'Walmart': 130.68,
    'Walt Disney': 119.34
}

financial_info ['Microsoft'] = 208.35
print (financial_info)




financial_info = {
    'American Express': 93.23,
    'Boeing': 178.44,
    'Coca-Cola': 45.15,
    'Nike': 97.99,
    'JPMorgan':96.27,
    'Walmart': 130.68,
    'Walt Disney': 119.34
}
nike_price = financial_info.get('Nike', None)
print (nike_price)
