from django.urls import path
from .views import MenuView

urlpatterns = [
    path("inicio/", MenuView.as_view(), name='inicio'),
]
