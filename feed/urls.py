from unicodedata import name
from django.urls import path


from . import views

app_name = 'feed'

urlpatterns = [
    path("", views.Homepage.as_view(), name="index")
]
