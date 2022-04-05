from django.urls import path
from .views import login_view, logout_view, register_view, verify_email_view
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView

urlpatterns = [
    path('password-reset', PasswordResetView.as_view()),
    path('custom-login', login_view),
    path('custom-logout', logout_view),
    path('custom-register', register_view),
    path('<int:user_id>/verify/<str:token>', verify_email_view)
]
