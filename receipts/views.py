from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from receipts.models import Receipt, ExpenseCategory, Account
from receipts.forms import (
    CreateForm,
    CategoryForm,
    AccountForm,
)


@login_required
def receipt_list(request):
    receipts = Receipt.objects.filter(purchaser=request.user)
    context = {"receipt_list": receipts}
    return render(request, "receipts/list.html", context)


@login_required
def create_receipt(request):
    if request.method == "POST":
        form = CreateForm(request.POST)
        if form.is_valid():
            receipt = form.save(False)
            receipt.purchaser = request.user
            receipt.save()
            return redirect("home")
    else:
        form = CreateForm()
    context = {
        "form": form,
    }
    return render(request, "receipts/create.html", context)


@login_required
def category_list(request):
    categories = ExpenseCategory.objects.filter(owner=request.user)
    context = {
        "categories": categories,
    }
    return render(request, "categories/list.html", context)


@login_required
def account_list(request):
    accounts = Account.objects.filter(owner=request.user)
    context = {
        "accounts": accounts,
    }
    return render(request, "accounts/list.html", context)


@login_required
def create_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(False)
            category.owner = request.user
            category.save()
            return redirect("category_list")
    else:
        form = CategoryForm()
    context = {
        "form": form,
    }
    return render(request, "categories/create.html", context)
