from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import Subscribe
from .forms import SubForm


def sub_form(request):
    """
    * A view to save visitors subscription form.
    """
    subscriber = get_object_or_404(
        Subscribe, email=request.email)
    if subscriber:
        messages.error(request, 'You are already a SUB!')
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
