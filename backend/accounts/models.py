from django.db import models
from django.contrib.auth.base_user import (AbstractBaseUser, BaseUserManager)
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone

class CustomUserManager(BaseUserManager):

    def create_user(self, email, mobile, password, first_name, last_name=None, profile_pic=None):
        user = self.model(email=email, mobile=mobile, first_name=first_name, last_name=last_name, profile_pic=profile_pic)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, mobile, password, first_name, last_name=None):
        user = self.model(email=email, mobile=mobile, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self.db)
        return user
        
def user_directory_path(instance, filename):
    return 'profile_pics/{0}_{1}'.format(instance.first_name, filename)

class User(AbstractBaseUser, PermissionsMixin):
    email       = models.EmailField(unique=True)
    first_name  = models.CharField(max_length=100)
    last_name   = models.CharField(max_length=100, blank=True, null=True)
    mobile      = models.IntegerField(unique=True)
    is_active   = models.BooleanField(default=True)
    is_staff    = models.BooleanField(default=True)
    is_admin    = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    profile_pic = models.ImageField(default='profile_pics/default.png', upload_to=user_directory_path)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('first_name', 'mobile')
 
    objects = CustomUserManager()

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
