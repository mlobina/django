from django.shortcuts import render
import csv
from django.conf import settings

def inflation_view(request):
    template_name = 'inflation.html'
    table_headers = ['Год', 'Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь',
                     'Октябрь', 'Ноябрь', 'Декабрь', 'Всего']
    inflation_list = []
    keys = ['Год', 'Янв', 'Фев', 'Мар', 'Апр', 'Май', 'Июн', 'Июл', 'Авг', 'Сен',
            'Окт', 'Ноя', 'Дек', 'Суммарная']
    # чтение csv-файла и заполнение контекста
    with open(settings.INFLATION_RUSSIA_CSV, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            inflation_list.append({'year': row['Год'], 'months': [row[month] for month in keys[1:-1]],
                                   'total': row['Суммарная']})

    context = {'headers': table_headers, 'keys': keys, 'inflation_list': inflation_list}
    return render(request, template_name,
                  context)