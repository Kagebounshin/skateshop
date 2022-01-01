from django.http import HttpResponse


class StripeWH_handler:
    """Handle Stripe Webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """ Handle A Generic/Unknown/Unexpected Webhook Event"""
        return HttpResponse(
            content=f'Unhandled Webhook Recieved: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """ Handle The payment_intent.succeeded Webhook From Stripe"""
        return HttpResponse(content=f'Webhook Recieved: {event["type"]}',
                            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """ Handle The Payment_intent.payment_failed Webhook From Stripe"""
        return HttpResponse(
            content=f'PAYEMENT FAILED Webhook Recieved: {event["type"]}',
            status=200)
