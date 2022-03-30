from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

# from core.forms import RegisterForm # AuthenticationForm - login uchun form
# from core.forms import RegisterForm
from .forms import LoginForm, RegisterForm
from django.contrib.auth import login, logout
from django.conf import settings
from django.contrib.auth import get_user_model

USER = get_user_model()
# USER = settings.AUTH_USER_MODEL

@login_required
def check_user(request):
    user = request.user # AnonymousUser  
    print(user.is_authenticated)
    return render(request, 'check_auth.html', {'user': user})

# @login_required(login_url='/users/login')
# def check_user(request):
#     user = request.user # AnonymousUser  
#     print(user.is_authenticated)
#     return render(request, 'check_auth.html', {'user': user})

def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'registration/registration_finish.html', {})
    
    return render(request, 'registration/register.html', {'form': form})


def login_view(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.get(username=username)
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL) # /users/check-user

    return render(request, "registration/login.html", {'form': form})


def logout_view(request):
    print(request.user) # AnonymousUser, <User: Admin>
    if request.user.is_authenticated:
        print('login qilgan')
    else:
        print('nomalum foydalanuvchi')
    logout(request)
    return redirect(settings.LOGOUT_REDIRECT_URL)


def register_view(request):
    form = RegisterForm(request.POST or None) # RegisterForm()

    if request.method == 'POST':
        if form.is_valid():
            fields = form.cleaned_data
            del fields['password_confirmation']
            user = USER.objects.create_user(**fields)
            # user.set_password(password)
            # user.save()
            return render(request, 'registration/registration_finish.html', {})
    
    return render(request, 'registration/register.html', {'form': form})
