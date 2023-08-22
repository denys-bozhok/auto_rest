from django.db import models
from django.utils.text import slugify


class Auto(models.Model):
    label = models.CharField(max_length=25, unique=True)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    slug = models.SlugField(editable=False)
    
    def __str__(self):
        return f'{self.label}, {self.year} : {self.price}'
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.label)
        super().save(*args, **kwargs)
        
        
class AutoPassport(models.Model):
    related_auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    number = models.IntegerField()
    prefix = models.CharField(max_length=2)
    
    def __str__(self):
        return f'{self.prefix}{self.number}'
        
class Owner(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    car_number = models.ForeignKey(AutoPassport, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'