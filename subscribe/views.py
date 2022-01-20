from django.shortcuts import render
from django.contrib import messages

from .forms import SubForm


def sub_form(request):
    """
    * A view to save visitors subscription form.
    # get all registered emails from database
    # Add new emails to database
    # Send confirmation Email
    """
    if request.method == 'POST':
        form = SubForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,
                             'You are now a Subscriber to our site, \
                             Thanks for joining us!')
        else:
            messages.error(request,
                           'Something went wrong, \
                            Please make sure that the form is valid!')
    else:
        form = SubForm()

    template = 'home/index.html'

    context = {
        'form': form
    }

    return render(request, template, context)
