from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class CustomUserManager(BaseUserManager):
    def create_user(self, mobile, password=None, **extra_fields):
        if not mobile:
            raise ValueError("Mobile number is required.")
        
        user = self.model(mobile=mobile, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, mobile, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_active', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        if extra_fields.get('is_active') is not True:
            raise ValueError('Superuser must have is_active=True.')
        
        return self.create_user(mobile, password, **extra_fields)

class Account(AbstractBaseUser, PermissionsMixin):
    cityName = models.ForeignKey('hpcl.CityModel', on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=100, blank=True, null=True)
    code = models.CharField(max_length=100, blank=True, null=True, unique=True)
    mobile = models.CharField(max_length=10, blank=True, null=True, unique=True)
    role = models.CharField(max_length=100, choices=[('ADMIN', 'ADMIN'),('HR', 'HR'), ('MIS', 'MIS'), ('WE', 'WE'),('CITYMANAGER', 'CITYMANAGER'),('SUPERVISOR', 'SUPERVISOR'), ('FWP', 'FWP')], default='Active')
    status = models.CharField(max_length=10, choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active')
    lock = models.CharField(max_length=10, choices=[('Lock', 'Lock'), ('UnLock', 'UnLock')], default='UnLock')
    password = models.CharField(max_length=128)
    
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'mobile'

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return self.is_staff
