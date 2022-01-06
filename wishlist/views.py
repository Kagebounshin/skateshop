from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def view_wishlist(request):
    """ View for wishlist page """

    template = 'wishlist/wishlist.html'
    return render(request, template)
