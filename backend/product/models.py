from django.db import models

# Create your models here.
from io import BytesIO
from PIL import Image
from email.policy import default
from django.core.files import File
from django.db import models
# from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser


"""This class will be a model called category"""
class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.slug}/'


"""This class will be a model called Profile"""
class Profile(AbstractUser):

    username = models.CharField(max_length=100, blank=True,unique=True)
    email = models.EmailField(max_length=100)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)

    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    dOB = models.DateField(blank=True, null=True, default="1999-01-22")
    phoneNumber = models.IntegerField(blank=True, null=True)

    addressLine1 = models.CharField(max_length=200, blank=True)
    addressLine2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    postcode = models.CharField(max_length=200, blank=True)
    country = models.CharField(max_length=200, blank=True)
    class Meta:
        ordering=['username']
    def __str__(self):
        return self.username

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''
    def to_dict(self):
        return{
            "username":self.username,
            "email":self.email,
            "image":self.image

        }

"""This class will be a model called Product"""
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    date_added = models.DateField(auto_now_add=True)
    date_finish =models.DateField(default='2020-01-31')
    user=models.ForeignKey(Profile, related_name='products', on_delete=models.CASCADE)
    email=models.EmailField(max_length=100)
    sold=models.CharField(max_length=10,default="unsold")

    
    class Meta:
        ordering = ('-date_finish',)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'
    
    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''
    
    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return 'http://127.0.0.1:8000' + self.thumbnail.url
            else:
                return ''
    
    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail

"""This class will be a model called Bids"""
class Bids(models.Model):

    user=models.ForeignKey(Profile, related_name='bids', on_delete=models.CASCADE)
    price=price = models.DecimalField(max_digits=6, decimal_places=2)
    product = models.ForeignKey(Product, related_name='products', on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ('price',)

    def __str__(self):
        return str(self.price)

"""This class will be a model called Questions"""
class Questions(models.Model):
    product=models.ForeignKey(Product, related_name='questions', on_delete=models.CASCADE)
    user=models.ForeignKey(Profile, related_name='questions', on_delete=models.CASCADE)
    question=models.CharField(max_length=500, blank=True)
    title=models.CharField(max_length=255, default='Title')

    
    
    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title
"""This class will be a model called Answers"""        
class Answers(models.Model):
    product=models.ForeignKey(Product, related_name='answers', on_delete=models.CASCADE)
    user=models.ForeignKey(Profile, related_name='answers', on_delete=models.CASCADE)
    question=models.ForeignKey(Questions,related_name='answers', on_delete=models.CASCADE)
    answer=models.CharField(max_length=500,blank=True)


    class Meta:
        ordering = ('answer',)

    def __str__(self):
        return self.answer
