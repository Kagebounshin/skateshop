from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect

from .models import Subscribe
from .forms import SubForm


def sub_form(request):
    """
    * A view to save visitors subscription form.
    # get all registered emails from database
    # Add new emails to database
    # Send confirmation Email
    """
    form = SubForm()

    if request.method == 'POST':
        form = SubForm(request.POST)
        emails = Subscribe.objects.values_list('email', flat=True)
        if request.POST['email'] in emails:
            messages.error(request, "You have already subscribed to our newsletter")
            return HttpResponseRedirect(request.path_info)
        elif form.is_valid():
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
        'form': form,
        'on_sub_page': True,
    }

    return render(request, template, context)
