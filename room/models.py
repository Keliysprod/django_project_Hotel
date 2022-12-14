from django.db import models

class Listings(models.Model):
    title=models.CharField('Загаловок', max_length=75)
    price=models.FloatField('Цена',default=0)
    num_bedrooms=models.IntegerField('Кол-во комнат')
    num_bathrooms=models.IntegerField('Кол-во ванн')
    square_footage=models.IntegerField('Площадь')
    address=models.CharField('Адресс', max_length=100)
    #image=


    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Список комнат'
        verbose_name_plural='Списки'
        ordering=('-price',)
