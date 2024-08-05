from django.db import models  # type: ignore
from django.contrib.auth import get_user_model  # type: ignore

from core.models import PublishedAndCreatedModel
from blog.constants import MAX_CHAR_FIELD_LENGTH

User = get_user_model()


class Category(PublishedAndCreatedModel):
    title = models.CharField(
        max_length=MAX_CHAR_FIELD_LENGTH, verbose_name='Заголовок')
    slug = models.SlugField(unique=True, verbose_name='Идентификатор',
                            help_text='Идентификатор страницы для URL; '
                            'разрешены символы латиницы, цифры, дефис и'
                            ' подчёркивание.'
                            )
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Location(PublishedAndCreatedModel):
    name = models.CharField(max_length=MAX_CHAR_FIELD_LENGTH,
                            verbose_name='Название места')

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        return self.name


class Post(PublishedAndCreatedModel):
    title = models.CharField(max_length=MAX_CHAR_FIELD_LENGTH,
                             verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    pub_date = models.DateTimeField(verbose_name='Дата и время публикации',
                                    help_text='Если установить дату и время в '
                                    'будущем — можно делать отложенные '
                                    'публикации.')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор публикации'
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL, null=True,
        verbose_name='Местоположение'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL, null=True,
        verbose_name='Категория'
    )

    class Meta:
        default_related_name = 'posts'
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'
        ordering = ('-pub_date',)

    def __str__(self):
        return self.title
