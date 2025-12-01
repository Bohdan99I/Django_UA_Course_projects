from django.db import models
from django.utils import timezone
from django.urls import reverse


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Назва тегу")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="Слаг")

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"
        ordering = ['name']

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="Слаг")
    content = models.TextField(verbose_name="Контент")
    published_date = models.DateTimeField(default=timezone.now, verbose_name="Дата публікації")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")
    updated_date = models.DateTimeField(auto_now=True, verbose_name="Дата оновлення")
    tags = models.ManyToManyField(Tag, related_name='articles', blank=True, verbose_name="Теги")
    is_published = models.BooleanField(default=True, verbose_name="Опубліковано")

    class Meta:
        verbose_name = "Стаття"
        verbose_name_plural = "Статті"
        ordering = ['-published_date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug': self.slug})
