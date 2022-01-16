from django.shortcuts import render


def index(request):
    """ View for index page """
    return render(request, 'home/index.html')
