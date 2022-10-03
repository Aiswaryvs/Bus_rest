from pyexpat import model
from re import T
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager, BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        
        if not email:
            raise ValueError('User must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None):
        
        user = self.create_user(
            email,
            password=password,
            name=name,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    username = None
    id = models.AutoField(primary_key=True,auto_created=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    
    def __str__(self):
        return self.name


class BusList(models.Model):
    id = models.AutoField(primary_key=True,auto_created=True)
    bus_no = models.CharField(max_length=100)
    bus_name = models.CharField(max_length=100)
    from_place = models.CharField(max_length=100)
    to = models.CharField(max_length=100)

    def __str__(self):
        return self.bus_name


class Reservation(models.Model):
    id = models.AutoField(primary_key=True,auto_created=True)
    bus = models.ForeignKey(BusList,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    current_date = models.DateTimeField(auto_now_add=True)
    reservation_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    

class Price(models.Model):
    bus = models.ForeignKey(BusList,on_delete=models.CASCADE)
    price = models.PositiveIntegerField()