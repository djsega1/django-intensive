# Generated by Django 3.2.16 on 2022-11-07 17:35

import catalog.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_item_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='upload',
            field=models.ImageField(default='default.jpg', upload_to='uploads/%Y/%m', verbose_name='превью'),
        ),
        migrations.AlterField(
            model_name='item',
            name='text',
            field=models.TextField(help_text='Описание должно быть больше чем из 2-ух слови содержать слова "превосходно" и "роскошно".', validators=[catalog.validators.item_text_validator], verbose_name='текст'),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='max 150 символов', max_length=150, verbose_name='Название')),
                ('upload', models.ImageField(upload_to='uploads/%Y/%m', verbose_name='фотография')),
                ('item', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='catalog.item', verbose_name='товар')),
            ],
            options={
                'verbose_name': 'фотография',
                'verbose_name_plural': 'фотографии',
            },
        ),
    ]
