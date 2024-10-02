from django.db import models

class Buyer(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя покупателя(username аккаунта)')
    balance = models.DecimalField(max_digits=6, decimal_places=1, verbose_name='Ваш баланс')
    age = models.IntegerField(verbose_name='Ваш возраст')

class Dogs(models.Model):
    breed_dogs = models.CharField(max_length=20)
    name_dogs = models.CharField(max_length=20)
    weight_dogs = models.IntegerField()

class Auto(models.Model):
    model_auto = models.CharField(max_length=20)
    power = models.IntegerField()
    year = models.IntegerField()
    color = models.CharField(max_length=20)
