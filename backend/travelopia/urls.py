from django.urls import path
from .views import MyView

urlpatterns = [
    path('my-url/', MyView.as_view(), name='my-view'),
]