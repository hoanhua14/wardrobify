from django.urls import path
from receipts.views import receipt_list

urlpatterns = [path("receipts/", receipt_list, name="receipt_list")]
# if i wanna put this url into a link, name goes into {% url name %}
# then django will go from main url => app's url
