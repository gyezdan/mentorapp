# Generated by Django 2.0.7 on 2020-06-24 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0001_initial'),
        ('users', '0007_auto_20200611_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='communities',
            field=models.ManyToManyField(to='communities.Community'),
        ),
    ]