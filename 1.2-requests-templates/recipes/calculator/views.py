from django.http import HttpResponse
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def hello(request, recipe):
    if recipe in [key for key in DATA]:
        list = []
        for key, value in DATA[recipe].items():
            list.append(f'{key}: {float(value)}')
        context = {
            'data': list
        }
        return render(request, 'hello.html', context)
    # яйца, шт: 2
    # молоко, л: 0.1
    # соль, ч.л.: 0.5
    else:
        return HttpResponse('Рецепт не найден!')
# {% for x in data % }
# <li>{{ x }}</li>
# {% endfor %}