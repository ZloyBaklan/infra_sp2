from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import UniqueConstraint

from titles.models import Title
from users.models import CustomUser


class Review(models.Model):
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE,
        verbose_name='Обозреваемое наименование', related_name='reviews'
    )
    text = models.TextField(max_length=10000, verbose_name='Текст обзора')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE,
                               verbose_name='Автор обзора')
    score = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        verbose_name='Рейтинг обзора'
    )
    pub_date = models.DateTimeField(auto_now_add=True,
                                    verbose_name='Дата публикации обзора')

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
        UniqueConstraint(fields=['author', 'text', 'score'], name='review')


class Comment(models.Model):
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, verbose_name='Обзор',
        related_name='comments'
    )
    text = models.TextField(max_length=1000, verbose_name='Текст коментария')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE,
                               verbose_name='Автор коментария')
    pub_date = models.DateTimeField(auto_now_add=True,
                                    verbose_name='Дата коментария')

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
