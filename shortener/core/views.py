from django.http import HttpResponse
from django.shortcuts import render, redirect

from shortener.core.models import UrlRedirect


# Create your views here.

def redirecting(requisition, slug):
    # return HttpResponse(f'Olá Django: {slug}')
    # return redirect('http://google.com')
    url_redirect = UrlRedirect.objects.get(slug=slug)
    return redirect(url_redirect)
