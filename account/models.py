from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from .validator import validate_phone


class UserManager(BaseUserManager):
    def create_user(self, phone, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not phone:
            raise ValueError("Users must have an phone number")

        user = self.model(
            phone=phone,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            phone,
            password=password,

        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    is_active = models.BooleanField(default=True, verbose_name='فعال ؟')
    is_admin = models.BooleanField(default=False, verbose_name='ادمین')
    phone = models.CharField(unique=True, max_length=12, verbose_name='شماره تلفن')
    validators = [validate_phone]
    objects = UserManager()

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.phone

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربرها'


class Otp(models.Model):
    phone = models.CharField(max_length=11, verbose_name='شماره تلفن')
    code = models.SmallIntegerField(verbose_name='کد ارسال شده')
    token = models.CharField(max_length=200, null=True, blank=True, verbose_name='توکن')

    def __str__(self):
        return self.phone


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='addresses', verbose_name='یوزر')
    fullname = models.CharField(max_length=50, verbose_name='نام و نام خانوادگی')
    phone = models.CharField(max_length=12, blank=True, null=True, verbose_name='شماره تلفن')
    address = models.CharField(max_length=300, verbose_name='آدرس')
    postal_code = models.PositiveSmallIntegerField(verbose_name='کد پستی')
    text = models.TextField(null=True, blank=True, verbose_name='توضیحات اضافه')

    def __str__(self):
        return self.user.phone

    class Meta:
        verbose_name = 'آدرس'
        verbose_name_plural = 'آدرس ها'
