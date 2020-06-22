from django.db import models
from item.models import Items
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse
# Create your models here.
class Order(models.Model):
    user=models.ForeignKey('auth.User', on_delete=models.CASCADE)
    first_name=models.CharField(max_length=256,blank=True, null=True)
    last_name=models.CharField(max_length=256,blank=True, null=True)
    phone= PhoneNumberField(blank=True, null=True)
    suma=models.FloatField(blank=True, null=True)
    city=models.CharField(max_length=256,blank=True, null=True)
    status=models.CharField(max_length=256,default='processing' ,choices=(('processing','Processing'),('paid','Paid'),('shiped','Shiped'),('complete','Complete'),('cancel','Cancel'),))
    creation_data=models.DateTimeField(auto_now_add=True)
    payment_data=models.DateTimeField(blank=True, null=True)
    manager=models.CharField(max_length=256, blank=True, null=True)
    delivery=models.CharField(max_length=256,choices=(('own','own pickup'),('DHL','DHL'),('New_Post','New Post'),))
    filial_number=models.PositiveIntegerField(blank=True, null=True)
    def get_absolute_url (self):
        return reverse('staff_order_update', kwargs={'pk':self.pk})
    def __str__(self):
        return str(self.pk)
    class Meta:
        ordering=['-creation_data']
class Particle(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    item=models.ForeignKey(Items,on_delete=models.CASCADE)
    amount=models.PositiveIntegerField()
    class Meta:
        unique_together=['order','item']
    def __str__(self):
        return str(self.order.pk)
class Promocodes(models.Model):
    name=models.CharField(max_length=256, unique=True)
    value=models.FloatField()
    def __str__(self):
        return self.name
