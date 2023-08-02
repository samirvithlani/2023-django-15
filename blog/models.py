from django.db import models

# Create your models here.
#Django ORM - Object Relational Mapper
#create table product(id,name varchar(200),price float,qty int,description varchar(500))
class Product(models.Model):
    name =models.CharField(max_length=200)
    price =models.FloatField()
    qty =models.IntegerField()
    description =models.TextField()
    color =models.CharField(max_length=15)
    saleunit = models.IntegerField(null=True)
    #blog_product
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table="product"
        
