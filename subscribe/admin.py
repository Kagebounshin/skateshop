from django.contrib import admin
from .models import Subscribe


class SubAdmin(admin.ModelAdmin):
    """ For Admin panel """
    list_display = ('email_address',)
    search_fields = ('email_address',)


admin.site.register(Subscribe, SubAdmin)