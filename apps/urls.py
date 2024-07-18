from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from apps.views import RegisterFormView, ProfileFormView, ProductListView

urlpatterns = [
    path('', LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('accounts/profile/', ProfileFormView.as_view(), name='profile'),
    path('auth/register', RegisterFormView.as_view(), name='register'),
    path('auth/login/profile/product_list', ProductListView.as_view(), name='product_list')
]
