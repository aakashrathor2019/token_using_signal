from django.urls import path
from .views import UserCreateView, TokenView

urlpatterns = [
    path('create-user/', UserCreateView.as_view(), name='create-user'),
    path('token/', TokenView.as_view(), name='token'),
]
