from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser, PermissionsMixin, UserManager

class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField('Email address', unique=True)
    is_staff = models.BooleanField(default=False,
        help_text='Designates whether the user can log into this admin site.',
    )
    is_active = models.BooleanField('active', default=True,
        help_text=(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField('Date joined', auto_now_add=True)

    USERNAME_FIELD = 'email' # null=False, unique=True

    REQUIRED_FIELDS = ['first_name']

    # objects = UserManager()