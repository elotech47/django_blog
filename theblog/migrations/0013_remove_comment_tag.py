# Generated by Django 3.0.2 on 2021-01-06 23:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0012_auto_20210107_0023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='tag',
        ),
    ]
