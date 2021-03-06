# Generated by Django 2.0.7 on 2020-06-10 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200609_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='basedCity',
            field=models.CharField(blank=True, default='', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='basedCountry',
            field=models.CharField(blank=True, default='', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='basedState',
            field=models.CharField(blank=True, default='', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='currentInstitute',
            field=models.CharField(blank=True, default='', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='currentStatus',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='profile',
            name='firstName',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AlterField(
            model_name='profile',
            name='homeCity',
            field=models.CharField(blank=True, default='', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='homeCountry',
            field=models.CharField(blank=True, default='', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='homeState',
            field=models.CharField(blank=True, default='', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='lastName',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AlterField(
            model_name='profile',
            name='major1',
            field=models.CharField(blank=True, default='', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='major2',
            field=models.CharField(blank=True, default='', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='minor1',
            field=models.CharField(blank=True, default='', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='minor2',
            field=models.CharField(blank=True, default='', max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='priorInstitute',
            field=models.CharField(blank=True, default='', max_length=120, null=True),
        ),
    ]
