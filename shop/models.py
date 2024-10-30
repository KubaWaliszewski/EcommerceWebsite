from django.db import models
from django.utils.text import slugify

from account.models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'categories'
        ordering = ('-created_at',)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


class Product(models.Model):
    user = models.ForeignKey(CustomUser, related_name='products', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=300, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    discount = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    stock = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='media/products/', default='media/products/default.jpg', blank=True, null=True)


    class Meta:
        ordering = ('-created_at',)
    
    def get_discounted_price(self):
        return self.price - (self.price * self.discount / 100)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.image:
            self.image = 'products/default.jpg'

        if not self.slug: 
            self.slug = slugify(self.name)  
        super(Product, self).save(*args, **kwargs)



class Review(models.Model):
    user = models.ForeignKey(CustomUser, related_name='reviews', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(default=5)
    comment = models.TextField(max_length=400, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return f"Review by {self.user.email} for {self.product.name} - {self.rating}/5"