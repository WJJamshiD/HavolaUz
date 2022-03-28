from django.urls import path
from .views import check_user, register, login_view, logout_view, register_view
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView

urlpatterns = [
    path('check-user', check_user),
    path('login', LoginView.as_view()),
    path('logout', LogoutView.as_view()),
    path('register', register),
    path('password-reset', PasswordResetView.as_view()),
    path('custom-login', login_view),
    path('custom-logout', logout_view),
    path('custom-register', register_view)
]
