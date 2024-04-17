from django.db import models

# Create your models here.

#model for products
class Products(models.Model):
    id = models.AutoField(primary_key=True, blank=False, null=False)
    gender = models.CharField(max_length=7, blank=False, null=False, default="FEMALE")
    productName = models.CharField(max_length=300, default="product", null=False, blank=False)
    productPrice = models.IntegerField(blank=False, null=False, default=0)
    productImage = models.CharField(max_length=600, blank=False, null=False)
    rating = models.IntegerField(blank=False, null=False, default=5)