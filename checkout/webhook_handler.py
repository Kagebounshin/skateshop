from django.http import HttpResponse


class StripeWH_handler:
    """Handle Stripe Webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """ Handle A Generic/Unknown/Unexpected Webhook Event"""
        return HttpResponse(content=f'Webhook Recieved: {event["type"]}',
                            status=200)
