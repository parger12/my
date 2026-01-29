email_visits = 1000 # количество визитов из рассылок
context_visits = 2500 # количество визитов из контекстной рекламы
email_purchases = 50 # количество покупок из рассылок
context_purchases = 100 # количество покупок из контекстной рекламы
email_conversion = email_purchases / email_visits
context_conversion = context_purchases / context_visits 
print('Конверсия рассылок: {:.0%}'.format(email_conversion))
print('Конверсия контекстной рекламы: {:.0%}'.format(context_conversion))

if context_conversion > email_conversion:
    print ('Вывод: контекстная реклама эффективнее')
elif context_conversion == email_conversion:
    print ('Конверсии равны, пора смотреть другие метрики')
else:
    print ('Вывод: рассылки эффективнее')