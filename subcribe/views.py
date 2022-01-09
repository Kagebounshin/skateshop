from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from .models import Subcribe
from .forms import SubForm


def sub_form(request):
    """ Save the users email to the database """