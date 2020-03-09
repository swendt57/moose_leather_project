from django.shortcuts import render
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
