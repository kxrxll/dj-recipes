import copy
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
    'butter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def recipe_handler(request, recipe):
    ingredients = copy.copy(DATA[recipe])
    context = {
        'recipe': ingredients
    }
    if request.GET:
        servings_number = int(request.GET['servings'])
        for item in context['recipe']:
            context['recipe'][item] *= servings_number
    return render(request, 'calculator/index.html', context)
