# Generated by Django 2.0.7 on 2020-06-10 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200610_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='currentStatus',
            field=models.CharField(blank=True, default='', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, default='', max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='firstName',
            field=models.CharField(blank=True, default='', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='lastName',
            field=models.CharField(blank=True, default='', max_length=120, null=True),
        ),
    ]