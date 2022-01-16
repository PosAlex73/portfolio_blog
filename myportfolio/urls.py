from django.urls import path
from myportfolio.views import General

urlpatterns = [
    path('', General.as_view(), name='general')
]