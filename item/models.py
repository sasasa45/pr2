from django.db import models
from PIL import Image
from django.db.models import Q
# Create your models here.
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'item_{0}/{1}'.format(instance.pk, filename)
class  MrPickles (models.Manager):
    def search(self,query =None):
        qs=self.get_queryset()

        if query is not None:
            parts=query.split(' ')
            if len(parts)>1:
                querysets=[]
                for part in parts:
                    compl_filter=(
                         Q(name__icontains=part)|
                         Q(text__icontains=part)|
                         Q(category__name__icontains=part))
                    querysets.append(qs.filter(compl_filter).distinct())
                x=None
                for i  in range(len(querysets)-1):
                    x=querysets[i+1].intersection(querysets[i],querysets[i+1])
                return x
            else:
                compl_filter=(
                                        Q(name__icontains=query)|
                                        Q(text__icontains=query)|
                                        Q(category__name__icontains=query)
                                     )
                qs=qs.filter(compl_filter).distinct()
                return qs
def expand2square(pil_img, background_color):
    width, height = pil_img.size
    if width == height:
        return pil_img
    elif width > height:
        result = Image.new(pil_img.mode, (width, width), background_color)
        result.paste(pil_img, (0, (width - height) // 2))
        return result
    else:
        result = Image.new(pil_img.mode, (height, height), background_color)
        result.paste(pil_img, ((height - width) // 2, 0))
        return result
class Categories(models.Model):
    name=models.CharField(max_length=256)
    pic1=models.ImageField(upload_to='categories', blank=True,null=True)
    pic2=models.ImageField(upload_to='categories', blank=True,null=True)
    pic3=models.ImageField(upload_to='categories', blank=True,null=True)
    def __str__(self):
        return self.name
class Items(models.Model):
    name=models.CharField(max_length=256)
    category=models.ForeignKey(Categories, on_delete=models.CASCADE)
    price=models.FloatField()
    text=models.TextField()
    quantity=models.PositiveIntegerField()
    picture_original=models.ImageField(upload_to=user_directory_path, blank=True,null=True)
    picture_changed=models.ImageField(blank=True,null=True)
    picture_detail=models.ImageField(blank=True,null=True)
    like=models.ManyToManyField('auth.User', blank=True)
    objects=MrPickles()

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     path=self.picture_original.path[:-4]+'C'+self.picture_original.path[-4:]
    #     path2=self.picture_original.path[:-4]+'D'+self.picture_original.path[-4:]
    #     new_picture=Image.open(self.picture_original.path)
    #     im_thumb = expand2square(new_picture, (255, 255, 255)).resize((300,300), Image.LANCZOS)
    #     im_thumb.save(path, quality=95)
    #     im_thumb2 = expand2square(new_picture, (255, 255, 255)).resize((500,500), Image.LANCZOS)
    #     im_thumb2.save(path2, quality=95)
    #     self.picture_changed=path
    #     self.picture_detail=path2
    #     super().save(*args, **kwargs)
    def __str__(self):
        return self.name
# def get_absolute_url(self):
#     return reverse('item:detail', kwargs={'pk':self.pk})
