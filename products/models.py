from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False, blank=False)
    description = models.CharField(max_length=250, null=False, blank=False)
    other_info = models.CharField(max_length=250, blank=True, default='')

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=150, null=False, blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_consignment = models.BooleanField(null=False, default=False)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='images', default='images/no_image.png')

    def __str__(self):
        return self.name


class Size(models.Model):
    size = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return self.name