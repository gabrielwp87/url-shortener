from django.db.models import Count
from django.db.models.functions import TruncDate
from django.shortcuts import render, redirect

from shortener.core.models import UrlRedirect, UrlLog


# Create your views here.

def reports(requisition, slug):
    url_redirect = UrlRedirect.objects.get(slug=slug)
    url_shortened = requisition.build_absolute_uri(f'/{slug}')
    redirects_by_date = list(
        UrlRedirect.objects.filter(
            slug=slug
        ).annotate(
            data=TruncDate('logs__created_in')
        ).annotate(
            clicks=Count('data')
        ).order_by('data')
    )
    context = {
        'shortener': url_redirect,
        'url_shortened': url_shortened,
        'redirects_by_date': redirects_by_date,
        'total_clicks': sum(r.clicks for r in redirects_by_date),
    }
    return render(requisition, 'shortener/report.html', context)


def redirecting(requisition, slug):
    url_redirect = (UrlRedirect.objects.get(slug=slug))
    UrlLog.objects.create(
        origin=requisition.META.get('HTTP_REFERER'),
        user_agent=requisition.META.get('HTTP_USER_AGENT'),
        host=requisition.META.get('HOST_HTTP'),
        ip=requisition.META.get('REMOTE_ADDR'),
        url_redirect=url_redirect
    )

    return redirect(url_redirect.destiny)
