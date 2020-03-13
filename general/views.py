from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed
from django.conf import settings


def index(request):
    """Displays the index page"""

    return render(request, 'index.html', {'page_title': 'Moose Leather', 'page_heading': 'Moose Leather',
                                          'page': '.home'})


def load_comments(request):
    """Displays the Disqus comments page"""

    return render(request, 'comments.html', {'page_title': 'Comments / Discussion',
                                             'page_heading': 'Comments / Discussion', 'page': '.comments',
                                             'CANONICAL_URL': settings.CANONICAL_URL})


def set_screen_width(request):
    if not request.is_ajax() or not request.method == 'POST':
        return HttpResponseNotAllowed(['POST'])
    request.session['screen-width'] = request.POST['width']
    return HttpResponse(200)
