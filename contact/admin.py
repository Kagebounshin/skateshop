from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    """ Display contact form in admin """
    list_display = (
        'full_name',
        'email_address',
        'subject',
        'message',
    )


admin.site.register(Contact, ContactAdmin)
