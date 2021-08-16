from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username,first_name, last_name, password=None):
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email, username, password, first_name, last_name):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )

        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractUser):
    INTEREST_CHOICES = {
        ('choice1', 'Choice1'),
        ('choice2', 'Choice2'),
        ('choice3', 'Choice3'),
    }
    email =             models.EmailField(verbose_name='email', max_length=60, unique=True)
    username =          models.CharField(max_length=30, unique=True)
    date_joined =       models.DateField(verbose_name='date joined', auto_now_add=True)
    last_login =        models.DateField(verbose_name='last login', auto_now=True)
    is_admin =          models.BooleanField(default=False)
    is_active =         models.BooleanField(default=True)
    is_staff =          models.BooleanField(default=False)
    is_superuser =      models.BooleanField(default=False)
    first_name =        models.CharField(verbose_name='first_name', max_length=30)
    last_name =         models.CharField(verbose_name='last_name', max_length=30)
    description =       models.TextField(default="")
    profile_image =     models.ImageField(null=True)
    header_image =      models.ImageField(null=True)
    interest =          models.CharField(default="", max_length=20, choices=INTEREST_CHOICES)


    USERNAME_FIELD = 'email' 
#this field means that when you try to sign in the username field will be the email 
#change it to whatever you want django to see as the username when authenticating the user
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name',]

    objects = CustomUserManager()

    def __str__(self):
        return self.username