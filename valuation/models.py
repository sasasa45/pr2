from django.db import models
from item.models import Items
from order.models import Order
# Create your models here.
class Rate(models.Model):
    item=models.ForeignKey(Items, on_delete=models.CASCADE)
    user=models.ForeignKey('auth.User', on_delete=models.CASCADE)
    rate=models.FloatField()
    class Meta:
        unique_together=['item','user']
class Comment(models.Model):
    item=models.ForeignKey(Items, on_delete=models.CASCADE)
    user=models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text=models.TextField()
    creat_date=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.creat_date
    class Meta:
        ordering=['-creat_date']
class AnswerComment(models.Model):
    comment=models.ForeignKey(Comment, on_delete=models.CASCADE)
    user=models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text=models.TextField()
    creat_date=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.creat_date
class OrderComment(models.Model):
    order=models.ForeignKey(Order, on_delete=models.CASCADE)
    text=models.TextField()
    creat_date=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.creat_date
    class Meta:
        ordering=['-creat_date']
