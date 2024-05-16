from django.contrib import admin
from .models import Client


class ClientAdmin(admin.ModelAdmin):
    list_display = ('id','first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name', 'email')


admin.site.register(Client, ClientAdmin)
