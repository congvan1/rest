# Generated by Django 4.1.3 on 2022-12-07 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rate',
            name='total',
        ),
    ]
