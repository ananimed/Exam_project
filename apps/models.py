from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, Model, ImageField, IntegerField
from django.db.models.fields import TextField, DecimalField


class User(AbstractUser):
    image = ImageField(upload_to='users/')
    phone_number = CharField(max_length=20, unique=True, null=True,
                             blank=True)
    age = IntegerField(blank=True, null=True)


class Category(Model):
    name = CharField(max_length=50, unique=True)


class Product(Model):
    name = CharField(max_length=50, unique=True)
    description = TextField()
    price = DecimalField(max_digits=10, decimal_places=2)
    image = ImageField(upload_to='products/')
