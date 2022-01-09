from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import SubForm


def sub_form(request):
    """ Save the users email to the database """
    if request.method == 'POST':
        form = SubForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,
                             'You are now a Subscriber to our site, \
                             Thanks for joining us!')
            return redirect(reverse('index'))
        else:
            messages.error(request,
                           'Something went wrong, \
                            Please make sure that the form is valid!')
    else:
        form = SubForm()()

    template = 'home/index.html'

    context = {
        'form': form
    }

    return render(request, template, context)