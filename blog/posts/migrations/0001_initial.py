# Generated by Django 4.0.4 on 2022-05-04 18:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('description', models.CharField(max_length=100)),
                ('img', models.CharField(max_length=120)),
                ('content', models.TextField()),
                ('created_at', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
