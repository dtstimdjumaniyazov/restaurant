from django.db import models
import datetime
from django.urls import reverse

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=30, null=False)
    quantity = models.DecimalField(max_digits=6, decimal_places=1)
    TBSP = 'tbsp'
    LBS = 'lbs'
    GRAMMS = 'gramms'
    EGGS = 'eggs'
    OUNCES = 'ounces'
    UNIT_MEASURE = [
        (TBSP, 'tbsp'), (LBS, 'lbs'), (GRAMMS, 'gramms'), (EGGS, 'eggs'), (OUNCES, 'ounces')
    ]
    unit = models.CharField(max_length=6, choices=UNIT_MEASURE, default=LBS, null=False)
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("ingredients")
    
    
class MenuItem(models.Model):
    title = models.CharField(max_length=30, null=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    def __str__(self):
        return self.title
    
class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=6, decimal_places=2)
    
    def get_absolute_url(self):
        return reverse("home")
    

class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateField(default=datetime.date.today)
    
    