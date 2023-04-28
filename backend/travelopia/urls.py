from django.urls import path
from .views import MyView

urlpatterns = [
    path('booking/', MyView.as_view(), name='my-view'),
]