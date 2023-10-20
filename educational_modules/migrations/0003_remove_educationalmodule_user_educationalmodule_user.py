# Generated by Django 4.2.5 on 2023-10-20 11:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('educational_modules', '0002_educationalmodule_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='educationalmodule',
            name='user',
        ),
        migrations.AddField(
            model_name='educationalmodule',
            name='user',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL, verbose_name='Создатель модуля'),
        ),
    ]
