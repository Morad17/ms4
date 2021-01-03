from django.db import models

#Categories for products
class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=150)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    #String method
    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

#All the products for sale
class Product(models.Model):

    GENDER_CHOICES = [('Men', 'Men'),('Women', 'Women'),('Unisex','Unisex')]
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=150)
    description = models.TextField()
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=False, default='Unisex')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    season_sales = models.BooleanField(blank=False, default=False)
    rrp = models.DecimalField(max_digits=6, decimal_places=2, null=True)

    def __str__(self):
        return self.name

#For Discounted and Seasonal Products
class Season(models.Model):

    ALL_SEASONS = [('winter','Winter'),('spring','Spring'),('summer','Summer'),('autumn','Autumn')]
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    season = models.CharField(choices=ALL_SEASONS, max_length=10, blank=False )
    month_start = models.CharField(max_length=150)
    month_finish = models.CharField(max_length=150)
    discount = models.DecimalField(max_digits=6, decimal_places=2, null=True)

    def __str__(self):
        return self.name
