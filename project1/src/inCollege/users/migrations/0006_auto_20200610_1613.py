# Generated by Django 2.0.7 on 2020-06-10 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200610_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profilePicture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]