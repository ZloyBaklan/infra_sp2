import datetime

from django.core.validators import MaxValueValidator
from django.db import models

CURRENT_DATETIME = datetime.datetime.now()


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    year = models.PositiveSmallIntegerField(
        db_index=True,
        validators=[MaxValueValidator(int(CURRENT_DATETIME.year))]
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='titles',
    )
    description = models.TextField(null=True, blank=True)
    genre = models.ManyToManyField(Genre, related_name='titles')

    def __str__(self):
        return self.name
