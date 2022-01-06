from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import UserContactForm


def contact(request):
    """ View for Contact page """
    if request.method == 'POST':
        form = UserContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message was sent successfully!')
            return redirect(reverse('contact'))
        else:
            messages.error(request,
                           'Something went wrong, Please make sure that the form is valid!')
    else:
        form = UserContactForm()

    template = 'contact/contact.html'

    context = {
        'form': form
    }

    return render(request, template, context)
