# Generated by Django 5.1.4 on 2024-12-20 14:06

import django.db.models.deletion
import profile.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CadetProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hours', models.PositiveIntegerField(default=0)),
                ('current_project', models.CharField(max_length=100, null=True)),
                ('past_projects', models.JSONField(null=True)),
                ('black_hole_day', models.DateField(default=profile.models.get_first_rank_days)),
                ('means_of_contact', models.JSONField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cadet_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
