from django.contrib import admin
from .models import Subscribe


class SubAdmin(admin.ModelAdmin):
    """ For Admin panel """
    list_display = ('email',)
    search_fields = ('email',)


admin.site.register(Subscribe, SubAdmin)
