# Generated by Django 2.0.7 on 2020-06-12 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.CharField(max_length=1200),
        ),
    ]