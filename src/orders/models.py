from django.db import models
from accounts.models import Customer
from books.models import Book

class Order(models.Model):
    total_price = models.PositiveIntegerField(default=0)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)

class OrderItem(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    quntity = models.PositiveIntegerField(default=0)

    def save(self,*args,**kwargs):
        self.order.total_price += self.book.price * self.quntity
        super(OrderItem,self).save(*args,**kwargs)
        self.order.save()



