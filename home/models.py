from django.db import models
from helpers.slugify import slugify

# status tuple
STATUS = (
    ('t', 'Terminado'),
    ('n', 'No terminado'),
    ('d', 'En desarrollo'),
)


def portfolio_item_image(instance, filename):
    ext = filename.split('.')[-1]
    file = '{}.{}'.format(slugify(instance.name), ext)
    return '{}/{}'.format('portfolio', file)


# Abstract class with common fields
class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# Class model with information of portfolio item
class PortfolioItem(TimeStamp):
    img = models.ImageField(
        verbose_name='Portada',
        upload_to=portfolio_item_image
    )
    name = models.CharField(
        verbose_name='Nombre del proyecto',
        max_length=150
    )
    status = models.CharField(
        verbose_name='Estado',
        choices=STATUS,
        max_length=1
    )
    year = models.SmallIntegerField(
        verbose_name='Año'
    )
    stack = models.CharField(
        verbose_name='Stack tecnológico',
        max_length=255
    )
    responsive = models.BooleanField(
        verbose_name='RWD',
        default=True
    )
    url = models.URLField(
        verbose_name='Url del proyecto',
        blank=True
    )
    repository = models.URLField(
        verbose_name='Url del repositorio',
        blank=True
    )
    order = models.SmallIntegerField(
        verbose_name='orden'
    )
    published = models.BooleanField(
        verbose_name='Publicado',
        default=False
    )

    class Meta:
        verbose_name = 'Portafolio'
        verbose_name_plural = 'Portafolio'

    def __str__(self):
        return '{}'.format(self.name)
