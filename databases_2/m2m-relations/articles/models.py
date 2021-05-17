from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, unique=True, verbose_name='Название')
    text = models.TextField(unique=True, verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    scopes = models.ManyToManyField('Scope',
                                  verbose_name='Разделы',
                                  related_name='articles',
                                  through='ArticleScope')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Scope(models.Model):

    topic = models.TextField(unique=True, verbose_name='Название раздела')

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'

    def __str__(self):
        return self.topic



class ArticleScope(models.Model):

    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        blank=False,
        null=False)

    scope = models.ForeignKey(
        Scope,
        on_delete=models.CASCADE,
        blank=False,
        null=False)

    is_main = models.BooleanField(verbose_name='Основной раздел', default=False)

    class Meta:
        ordering = ['-is_main']

    def __str__(self):
        return f'Статья {self.article} из раздела {self.scope}'

