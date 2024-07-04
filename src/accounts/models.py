from django.db import models
from django.contrib.auth.models import User,UserManager

class CustomerManager(UserManager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(is_customer=True)

class Customer(User):
    is_customer = models.BooleanField(default=True)
    objects = CustomerManager()

    class Meta:
        verbose_name = "Customer"

    def save(self,*args,**kwargs):
        self.is_staff = False
        super(Customer,self).save(*args,**kwargs)


class AutherManager(UserManager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(is_auther=True)

class Auther(User):
    is_auther = models.BooleanField(default=True)
    objects = AutherManager()

    class Meta:
        verbose_name = "Auther"

    def save(self,*args,**kwargs):
        self.is_staff = False
        super(Auther,self).save(*args,**kwargs)