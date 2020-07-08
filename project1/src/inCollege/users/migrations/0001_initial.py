# Generated by Django 2.0.7 on 2020-06-09 19:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=120)),
                ('lastName', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('homeCity', models.CharField(blank=True, max_length=120, null=True)),
                ('homeState', models.CharField(blank=True, max_length=120, null=True)),
                ('homeCountry', models.CharField(blank=True, max_length=120, null=True)),
                ('priorInstitute', models.CharField(blank=True, max_length=120, null=True)),
                ('priorGradYear', models.PositiveSmallIntegerField(default=0, null=True)),
                ('basedCity', models.CharField(blank=True, max_length=120, null=True)),
                ('basedState', models.CharField(blank=True, max_length=120, null=True)),
                ('basedCountry', models.CharField(blank=True, max_length=120, null=True)),
                ('currentInstitute', models.CharField(blank=True, max_length=120, null=True)),
                ('currentGradYear', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('currentStatus', models.CharField(max_length=120)),
                ('major1', models.CharField(blank=True, max_length=120, null=True)),
                ('major2', models.CharField(blank=True, max_length=120, null=True)),
                ('minor1', models.CharField(blank=True, max_length=120, null=True)),
                ('minor2', models.CharField(blank=True, max_length=120, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
