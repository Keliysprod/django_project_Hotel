# Generated by Django 4.1.4 on 2022-12-14 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75, verbose_name='Загаловок')),
                ('price', models.FloatField(default=0, verbose_name='Цена')),
                ('num_bedrooms', models.IntegerField(verbose_name='Кол-во комнат')),
                ('num_bathrooms', models.IntegerField(verbose_name='Кол-во ванн')),
                ('square_footage', models.IntegerField(verbose_name='Площадь')),
                ('address', models.CharField(max_length=100, verbose_name='Адресс')),
            ],
            options={
                'verbose_name': 'Список комнат',
                'verbose_name_plural': 'Списки',
                'ordering': ('-price',),
            },
        ),
    ]
