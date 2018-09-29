
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home (request):
    return HttpResponse('Home Page!')

def items (request):
    return HttpResponse('Welcome to localhost/items')

def special_case_2003 (request):
    return HttpResponse('Welcome to localhost/items/2003')


def year_archive (request, a):
    return HttpResponse('Welcome to localhost/items/[0-9]{4,5}! %a' %a)


def month_archive (request, year, month):
    return HttpResponse('Welcome to localhost/items/[0-9]{4,5}!')


def day_archive (request, year, month, day):
    return HttpResponse('Welcome to localhost/item/(?P<year>[\d]{4))/(?P<month>[0-9]{2})/(?P<day>[\d]{2})')

def page (request, num = '1'):
    if num == '1':
        return HttpResponse('Вы перешли на первую страницу книги')
    else:
        return HttpResponse ('Вы перешли на страницу %s' %num)