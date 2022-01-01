from django.http import HttpResponse


class StripeWH_Handler:
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
        intent = event.data.object
        print(intent)
        return HttpResponse(content=f'Webhook Recieved: {event["type"]}',
                            status=200)
