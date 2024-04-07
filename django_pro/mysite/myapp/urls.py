from django.urls import path
from .views import index, contacts, index_item

urlpatterns = [
    path("hello/", index),
    path("hello/<int:id>", index_item),
    path("contacts/", contacts),
]