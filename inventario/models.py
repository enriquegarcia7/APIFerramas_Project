from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    description = models.TextField(max_length=500, blank=True)
    price = models.IntegerField()
    images = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    categorys = [
        ('Herramientas', 'Herramientas'),
        ('Vestimenta', 'Vestimenta'),
        ('Materiales', 'Materiales'),
        ('Otros', 'Otros'),
    ]
    category = models.CharField(
        max_length=50,
        choices=categorys,
        default='Herramientas',
    )

    def __str__(self):
        return self.product_name
