from django.db import models

from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=125, verbose_name="Название")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Post(models.Model):
    image = models.ImageField(upload_to="posts/", verbose_name="Изображение")
    title = models.CharField(max_length=125, verbose_name="Заголовок")
    description = models.TextField(max_length=500, verbose_name="Описание")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    location = models.CharField(max_length=125, verbose_name="Место проведения")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    
    def __str__(self):
        return f"{self.title} - {self.category} - {self.created_at}"
    
    class Meta:
        verbose_name = "Публикация"
        verbose_name_plural = "Публикации"