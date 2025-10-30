from django.urls import path
from account.api.v1.views import RegisterUser

account_urlpatterns = [
    path('register/', RegisterUser.as_view({'post': 'register'}), name='user-register'),

]
