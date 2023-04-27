from django.db import models

# Create your models here.
from django.template.defaultfilters import slugify


class Category(models.Model):
    title = models.CharField(verbose_name="Название Категории", max_length=150, unique=True)
    slug = models.SlugField(blank=True, null=True, unique=True)


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"



class Brand(models.Model):
    title = models.CharField(verbose_name="Название Бренда", max_length=150, unique=True)
    slug = models.SlugField(blank=True, null=True, unique=True)


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Бренд"
        verbose_name_plural = "Бренды"


class Product(models.Model):
    title = models.CharField(verbose_name="Название товара", max_length=150, unique=True)
    descr = models.TextField(verbose_name="Описание товара")
    price = models.IntegerField(verbose_name="Стоимость товара")
    quantity = models.IntegerField(verbose_name="Кол-во товаров")
    is_available = models.BooleanField(verbose_name="Есть в наличие?", default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукт"




class ProductImage(models.Model):
    photo = models.ImageField(verbose_name="Фото", upload_to="products/", blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
