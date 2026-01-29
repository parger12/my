email_visits = 1000 # количество визитов из рассылок
context_visits = 2500 # количество визитов из контекстной рекламы
email_purchases = 50 # количество покупок из рассылок
context_purchases = 100 # количество покупок из контекстной рекламы
email_conversion = email_purchases / email_visits
context_conversion = context_purchases / context_visits 
print (f'Конверсия рассылок: {email_conversion}%')
print (f'Конверсия контекстной рекламы: {context_conversion}% ')