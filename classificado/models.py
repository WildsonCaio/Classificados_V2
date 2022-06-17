from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Category(models.Model):
    name    =   models.CharField(max_length=255)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name        = 'Category'
        verbose_name_plural = 'Categories'

class Adverts(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    title       = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    category    = models.ForeignKey(Category, on_delete=models.CASCADE)
    image_1     = CloudinaryField()
    image_2     = CloudinaryField(blank=True)
    image_3     = CloudinaryField(blank=True)
    city        = models.CharField(max_length=30)
    district    = models.CharField(max_length=30)
    contact_1   = models.CharField(max_length=20)
    contact_2   = models.CharField(max_length=20, blank=True)
    price       = models.CharField(max_length=20)
    date        = models.DateField()
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name        = 'Adverts'
        verbose_name_plural = 'Adverts'
                

class FeedBack(models.Model):
    user     = models.ForeignKey(User, on_delete=models.CASCADE)
    subject  = models.CharField(max_length=255)
    feedback = models.TextField()
    def __str__(self):
        return self.user.username, self.subject
    
    
    class Meta:
        verbose_name        = 'FeedBack'
        verbose_name_plural = 'FeedBack'
    