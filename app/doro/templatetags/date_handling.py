from django import template
from food.models import Meal
from django.utils.timezone import now

register = template.Library()


@register.filter
def month_name(month_number):
    month_number = int(month_number)
    print(now().month)
    if now().month == month_number:
        print('aiiiija')
        return f'<strong style="text-decoration: underline;">{Meal.MONTH_CHOICES[month_number-1][1]}</strong>'
    return Meal.MONTH_CHOICES[month_number-1][1]
