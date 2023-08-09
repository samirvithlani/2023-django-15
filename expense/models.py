from django.db import models
from userapp.models import User

# Create your models here.

class ExpCategory(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        db_table = 'expcategory'
        
    def __str__(self):
        return self.name

class Expense(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    category = models.ForeignKey(ExpCategory,on_delete=models.CASCADE)    
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'expense'
    
    def __str__(self):
        return self.name    
    
    
