from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from receipts.models import Receipt


def receipt_list(request):
    receipts = Receipt.objects.all()
    context = {"receipt_list": receipts}
    return render(request, "receipts/list.html", context)
