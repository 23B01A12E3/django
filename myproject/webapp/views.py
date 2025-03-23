from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def homepages(request):
    return HttpResponse("Welcome to new homepages")
def firstweb(request):
    return HttpResponse("This is my first web page")
def secondweb(request):
    return HttpResponse("This is my second web page")
def htmlpage(request):
    template=loader.get_template('mytemp.html')
    return HttpResponse(template.render())   