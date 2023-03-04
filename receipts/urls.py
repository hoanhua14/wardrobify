from django.urls import path
from receipts.views import receipt_list, create_receipt

urlpatterns = [
    path("", receipt_list, name="home"),
    path("create/", create_receipt, name="create_receipt"),
]
# if i wanna put this url into a link, name goes into {% url name %}
# then django will go from main url => app's url
