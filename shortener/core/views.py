from django.http import HttpResponse
from django.shortcuts import render, redirect

from shortener.core.models import UrlRedirect


# Create your views here.

def reports(requisition, slug):
    url_redirect = UrlRedirect.objects.get(slug=slug)
    url_shortened = requisition.build_absolute_uri(f'/{slug}')
    context = {
        'shortener': url_redirect,
        'url_shortened': url_shortened,
    }
    return render(requisition, 'shortener/report.html', context)


def redirecting(requisition, slug):
    # return HttpResponse(f'Olá Django: {slug}')
    # return redirect('http://google.com')
    url_redirect = (UrlRedirect.objects.get(slug=slug))
    return redirect(url_redirect.destiny)
