# Generated by Django 4.1.1 on 2022-10-13 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0017_project'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': 'Проект', 'verbose_name_plural': 'Проекты'},
        ),
    ]
