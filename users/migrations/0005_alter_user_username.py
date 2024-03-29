# Generated by Django 3.2.16 on 2022-11-28 18:29

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, error_messages={'unique': 'Пользователь с таким адресом уже существует'}, help_text='Не более 150 символов. Буквы, цифры и @/./+/-/_ .', max_length=150, null=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator], verbose_name='имя пользователя'),
        ),
    ]
