from django.contrib import admin
from .models import Subcribe


class SubAdmin(admin.ModelAdmin):
    """ For Admin to see at the admin panel """
    list_display = ('email_address',)
    search_fields = ('email_address',)


admin.site.register(Subcribe, SubAdmin)