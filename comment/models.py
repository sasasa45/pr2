from django.db import models
from item.models import Items
# Create your models here.
class Comments(models.Model):
    item=models.ForeignKey(Items, on_delete=models.CASCADE)
    user=models.ForeignKey('auth.USER',on_delete=models.CASCADE)
    text=models.TextField()
    creation_date=models.DateTimeField(auto_now=True)
    
