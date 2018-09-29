from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def blog_articles (request, a, b):
    return HttpResponse('blog_article')

def comments (request, page_number):
    return HttpResponse('comments %s' %page_number)

def optional_args (request, year, foo):
    return HttpResponse('optional_args %s' %foo)

def report (request, id = '1'):
    return HttpResponse('comments %s' %id)

def hystory (request, page_slug, page_id):
    return HttpResponse('hystory')

def edit (request, page_slug, page_id):
    return HttpResponse('edit')


def discuss (request, page_slug, page_id):
    return HttpResponse('discuss')


def permissions (request, page_slug, page_id):
    return HttpResponse('permissions')