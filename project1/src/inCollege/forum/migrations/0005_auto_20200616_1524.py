# Generated by Django 2.0.7 on 2020-06-16 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_auto_20200612_1640'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('date_posted',)},
        ),
    ]
