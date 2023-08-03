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


#one author can have many books....        

class Author(models.Model):
    name =models.CharField(max_length=200)
    email =models.EmailField()
    age =models.IntegerField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table="author"

#

class Publication(models.Model):
    pname = models.CharField(max_length=200)
    year = models.IntegerField()
    city = models.CharField(max_length=200)
    
    class Meta:
        db_table="publication"
        
genere = (("Science","Science"),("Fiction","Fiction"),("Drama","Drama"),("Action","Action"))
class Books(models.Model):
    bname = models.CharField(max_length=200)
    bprice = models.FloatField()
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    book_genere = models.CharField(max_length=20,choices=genere)
    publication = models.ForeignKey(Publication,on_delete=models.CASCADE,null=True)
    
    class Meta:
        db_table="books"

        
