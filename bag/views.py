from django.shortcuts import render

# Create your views here.

def view_bag(request):
    """ View for rendering the bag content """
    return render(request, 'bag/bag.html')
