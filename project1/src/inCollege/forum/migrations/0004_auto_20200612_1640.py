# Generated by Django 2.0.7 on 2020-06-12 21:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_auto_20200612_1628'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment',
            new_name='commentcontent',
        ),
    ]
