# Generated by Django 3.2.16 on 2022-11-14 19:35

import catalog.validators
import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_auto_20221109_1657'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='is_on_main',
            field=models.BooleanField(default=False, verbose_name='на главной'),
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.ForeignKey(help_text='выберите категорию', on_delete=django.db.models.deletion.CASCADE, to='catalog.category', verbose_name='категория'),
        ),
        migrations.AlterField(
            model_name='item',
            name='text',
            field=ckeditor.fields.RichTextField(help_text='описание должно быть больше чем из 2-ух слови содержать слова "превосходно" и "роскошно".', validators=[catalog.validators.item_text_validator], verbose_name='текст'),
        ),
    ]
