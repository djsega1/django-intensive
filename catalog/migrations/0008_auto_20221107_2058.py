# Generated by Django 3.2.16 on 2022-11-07 17:58

import catalog.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_auto_20221107_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='upload',
            field=models.ImageField(default='default.jpg', upload_to='uploads/%Y/%m', verbose_name='изображение'),
        ),
        migrations.AlterField(
            model_name='item',
            name='text',
            field=models.TextField(help_text='Описание должно быть больше чем из 2-ух слови содержать слова "превосходно" и "роскошно".', validators=[catalog.validators.item_text_validator], verbose_name='текст'),
        ),
        migrations.AlterField(
            model_name='item',
            name='upload',
            field=models.ImageField(default='default.jpg', upload_to='uploads/%Y/%m', verbose_name='изображение'),
        ),
    ]