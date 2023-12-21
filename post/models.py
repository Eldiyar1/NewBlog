from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class HashTag(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Хештег"
        verbose_name_plural = "Хештеги"


class Product(models.Model):
    image = models.ImageField(upload_to='products', null=True, blank=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    rate = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    hashtags = models.ManyToManyField(HashTag, blank=True, related_name='products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name='products')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class Comment(models.Model):
    product = models.ForeignKey('post.Product', on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Коментарии"
        verbose_name_plural = "Коментарий"
