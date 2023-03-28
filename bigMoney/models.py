from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.


class Address(models.Model):
    RecipiantName = models.CharField(max_length=255)
    StreetAddress = models.CharField(max_length=255)
    City = models.CharField(max_length=255)
    State = models.CharField(max_length=20)
    zipcode = models.IntegerField()


class merchandise(models.Model):
    title = models.CharField(max_length=255)
    date_posted = models.DateTimeField(default=timezone.now)
    cost = models.FloatField()
    description = models.CharField(max_length=1024)
    image = models.ImageField(default='default.jpg', upload_to="merchandise_pics")
    quantity_in_stock = models.IntegerField()


class shoppingCart(models.Model):
    name = models.CharField(max_length=255)
    items = models.ManyToManyField(merchandise)


class Order(models.Model):
    name = models.CharField(max_length=255)
    date_ordered = models.DateTimeField(default=timezone.now)
    Orders = models.ManyToManyField(shoppingCart)


class User(AbstractUser):
    USER_ROLES = (
        ("S", "Seller"),
        ("C", "Customer")
    )
    role = models.CharField(max_length=1, blank=False, choices=USER_ROLES, default="S")
    
    
    email = models.EmailField(max_length=255, default="")
    name = models.CharField(max_length=255, default="New User")
    balance = models.FloatField(default=0.0)

    #IMPORT THE FOLLOWING
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True)
    

    # specific to seller, not accessible by customer
    available_merch = models.ManyToManyField(merchandise, default=None)

    # specific to customer, not accessible by seller
    ShoppingCart = models.ForeignKey(shoppingCart, on_delete=models.CASCADE, null=True)
    Orders = models.ManyToManyField(Order, default=None)
    
    
    def __str__(self):
        return f'{self.user.username} ({self.role})'


