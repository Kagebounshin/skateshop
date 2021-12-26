from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KAvLUIyDn1HnQXRLofck57upbHbuGmjg5SiuOOrnHLhFFmnq02mpkLQgbdnIpR55etWUVExBtBQOzs2uP3tYuSL00Rj8n2Kie',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
