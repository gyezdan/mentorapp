# Generated by Django 2.0.7 on 2020-07-07 16:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0008_profile_communities'),
    ]

    operations = [
        migrations.CreateModel(
            name='MentorRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_status', multiselectfield.db.fields.MultiSelectField(choices=[('A', 'Accepted'), ('R', 'Rejected')], max_length=3)),
                ('request_message', models.CharField(blank=True, default='', max_length=120, null=True)),
                ('request_from', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='sentby', to=settings.AUTH_USER_MODEL)),
                ('request_to', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='receivedby', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='mentors',
            field=models.ManyToManyField(related_name='mentors', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='profile',
            name='requests',
            field=models.ManyToManyField(to='users.MentorRequest'),
        ),
    ]
