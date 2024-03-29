# Generated by Django 3.2.16 on 2022-11-09 13:57

import catalog.validators
import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_auto_20221107_2058'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Image',
            new_name='Gallery',
        ),
        migrations.AlterModelOptions(
            name='gallery',
            options={'verbose_name': 'изображение', 'verbose_name_plural': 'галерея'},
        ),
        migrations.AlterField(
            model_name='item',
            name='text',
            field=ckeditor.fields.RichTextField(help_text='Описание должно быть больше чем из 2-ух слови содержать слова "превосходно" и "роскошно".', validators=[catalog.validators.item_text_validator], verbose_name='текст'),
        ),
        migrations.CreateModel(
            name='Preview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload', models.ImageField(default='default.jpg', upload_to='uploads/%Y/%m', verbose_name='изображение')),
                ('item', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='catalog.item', verbose_name='товар')),
            ],
            options={
                'verbose_name': 'превью',
                'verbose_name_plural': 'превью',
            },
        ),
    ]
