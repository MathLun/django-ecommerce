from django.db import models

# Create your models here.
class Products(models.Model):
    product_name = models.CharField(max_length=200),
    pub_date = models.DateTimeField('date publish')
