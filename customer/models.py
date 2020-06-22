from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.pk, filename)
class Customer (models.Model):
    user=models.OneToOneField('auth.User', on_delete=models.CASCADE )
    birth_date=models.DateField(blank=True,null=True)
    phone= PhoneNumberField(blank=True, null=True)
    city=models.CharField(max_length=256,blank=True, null=True)
    deliv_company=models.CharField(max_length=256,blank=True, null=True, choices=(('new_post','New Post'),('dhl','DHL')))
    filial_number=models.PositiveIntegerField(blank=True, null=True)
    picture=models.ImageField(upload_to=user_directory_path,blank=True, null=True)

    def __str__(self):
        return self.user.username
