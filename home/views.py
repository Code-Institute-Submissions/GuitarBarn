""" Views for Home app """
from django.shortcuts import render


def index(request):
    """ A view to return an index page """

    return render(request, 'home/index.html')
