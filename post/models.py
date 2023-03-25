from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=100, null=True, blank=True)
    text = models.TextField(verbose_name='Текст')
    image = models.ImageField(verbose_name='Изображение', blank=True, upload_to='images')

    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE, to_field='username')
    date_created = models.DateField(verbose_name='Дата создания', auto_now_add=True)
    date_updated = models.DateField(verbose_name='Дата редактирования', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['date_created']


class Comment(models.Model):
    author = models.ForeignKey(User, verbose_name='Комментарий', on_delete=models.CASCADE, to_field='username')
    text = models.TextField(verbose_name='Текст', max_length=500)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    date_created = models.DateField(verbose_name='Дата создания', auto_now_add=True)
    date_updated = models.DateField(verbose_name='Дата редактирования', auto_now=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['date_created']
