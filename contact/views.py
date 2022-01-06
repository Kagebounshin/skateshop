from django.shortcuts import render


def contact(request):
    """ View for wishlist page """

    template = 'contact/contact.html'
    return render(request, template)
