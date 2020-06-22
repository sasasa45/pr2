from django.contrib import admin
from .models import Order, Particle, Promocodes
# Register your models here.
admin.site.register(Order)
admin.site.register(Particle)
admin.site.register(Promocodes)
