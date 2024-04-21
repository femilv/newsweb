from django.db import models

class Category(models.Model):
    name = models.CharField(max_length =100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name



class News(models.Model):
    title = models.CharField(max_length = 200)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    images = models.ImageField(upload_to='images/', blank = True, null =True)
    created_at = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name_plural = "News"

    def __str__(self):
        return self.title
