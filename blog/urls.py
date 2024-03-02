from django.urls import path
from .views import MyView

urlpatterns = [
    path('hello/', MyView.as_view(), name='hello'),
]
