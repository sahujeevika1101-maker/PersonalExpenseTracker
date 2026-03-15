from django.db import models
from django.contrib.auth.models import User

class Expense(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True)
    title = models.CharField(max_length=100)
    amount = models.FloatField()
    category = models.CharField(max_length=50)
    date = models.DateField()

    def __str__(self):
        return self.title


class Income(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True)
    source = models.CharField(max_length=100)
    amount = models.FloatField()
    date = models.DateField()

    def __str__(self):
        return self.source