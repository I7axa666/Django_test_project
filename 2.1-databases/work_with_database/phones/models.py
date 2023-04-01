from django.db import models


class Phone(models.Model):

    # TODO: Добавьте требуемые поля
    name = models.CharField(max_length=50)
    price = models.FloatField()
    image = models.CharField(max_length=100)
    release_data = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.CharField(max_length=50)

    # def __str__(self):
    #     return f'{self.name}'
