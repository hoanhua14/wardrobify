from django import forms
from receipts.models import Receipt, ExpenseCategory, Account


class CreateForm(forms.ModelForm):
    class Meta:
        model = Receipt
        fields = ("vendor", "total", "tax", "date", "category", "account")
