from django.contrib import admin
from account.models import Account

# Register your models here.

# admin.register.site(Account)

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    pass

