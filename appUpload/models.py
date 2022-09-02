from django.db import models

# Create your models here.
STATUS = [
    ('draft', 'Draft'),
    ('published', 'Published'),
   ]
class Comment(models.Model):
  first_name = models.CharField(max_length=20)
  last_name = models.CharField(max_length=40)
  email = models.EmailField(max_length=50)
  phone = models.CharField(max_length=15)
  subject = models.CharField(max_length=30)
  user_comment = models.CharField(max_length=256)
  publish_date = models.DateTimeField(auto_now_add=True)
  status = models.CharField(max_length=10 , choices=STATUS, default="Draft")
  
  def __str__(self):
    return f'{self.first_name} - {self.last_name} - {self.subject}'
  
class Products(models.Model):
  title1 = models.CharField(max_length=20)
  title2 = models.CharField(max_length=20)
  price1 = models.IntegerField()
  price2 = models.IntegerField()
  image1 = models.ImageField(upload_to="img")
  image2 = models.ImageField(upload_to="img")
  image3 = models.ImageField(upload_to="img")
  content = models.CharField(max_length=500)
  category = models.CharField(max_length=20)
  installation = models.CharField(max_length=500)
  dimensions = models.CharField(max_length=100)
  status = models.CharField(max_length=10 , choices=STATUS, default="Draft")
  
  def __str__(self):
    return f'{self.title1} - {self.price1} - {self.category}'
  
  
  
  
  