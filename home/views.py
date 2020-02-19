from django.shortcuts import render

# TODO verify that the viewport setting in base.html allows users to zoom

def index(request):
    """Displays the index page"""
    return render(request, 'index.html', {'page_title': 'Moose Leather', 'page_heading': 'Moose Leather', 'page': '.home'})
