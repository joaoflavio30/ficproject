# Generated by Django 5.1.3 on 2024-12-18 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cadete',
            fields=[
                ('id_cadete', models.AutoField(primary_key=True, serialize=False)),
                ('login', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('current_project', models.CharField(blank=True, max_length=100, null=True)),
                ('recommended_project', models.CharField(blank=True, max_length=100, null=True)),
                ('past_projects', models.JSONField(blank=True, null=True)),
                ('black_hole', models.FloatField(default=0.0)),
                ('hours', models.PositiveIntegerField(default=0)),
                ('means_of_contact', models.JSONField(blank=True, null=True)),
                ('contact', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]