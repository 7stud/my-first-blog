from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^mypage/', views.greeting, name="greeting"),
]
