from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.


def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())


def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render())


def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())


def tracker(request):
    template = loader.get_template('tracker.html')
    return HttpResponse(template.render())


def search(request):
    template = loader.get_template('search.html')
    return HttpResponse(template.render())


def productview(request):
    template = loader.get_template('productview.html')
    return HttpResponse(template.render())


def checkout(request):
    template = loader.get_template('checkout.html')
    return HttpResponse(template.render())


