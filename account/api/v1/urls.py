from django.urls import path


account_urlpatterns = [
    path('accounts/', views.AccountListView.as_view(), name='account-list'),

]
