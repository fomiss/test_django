from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse


# Create your views here.
def hello_response (request):
    return HttpResponse('hello django response')

def http_redirect (request):
    return redirect('/lesson-two-response/fun1/')

def fun1 (request):
    return HttpResponse('hello fun1')

def render_html(reqest):
    _html = """
            <html>
        <head><title>TITLE</title>
            <body>
                <h1>HELLO HTML</h1>
            </body>
             </html>
    """
    return HttpResponse(_html)

def render_template(request):
    return render (request, 'mail.html', {})


def func_render_to_response (request):
    return render_to_response ('mail_render.html', {})

def form_hendler (request):
    if request.POST:
        return HttpResponse ('Request is POST')
    else:
        return HttpResponse ('Request is GET')