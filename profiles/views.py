from django.shortcuts import render


def profile(request):
    """ Display Users Profile """
    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)
