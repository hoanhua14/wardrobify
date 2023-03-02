from django.contrib import admin
from receipts.models import ExpenseCategory, Account, Receipt

# Register your models here.


@admin.register(ExpenseCategory, Account, Receipt)
class ExpenseCategory(admin.ModelAdmin):
    list_display = ()


class Account(admin.ModelAdmin):
    list_display = ()


class Receipt(admin.ModelAdmin):
    list_display = ()
