from django.contrib import admin
from bank.models import banks
from bank.models import bankclient

# Register your models here.
admin.site.register(banks)
admin.site.register(bankclient)