# Generated by Django 5.1 on 2024-09-18 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tile', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
                ('seats', models.IntegerField(max_length=100)),
                ('fee', models.IntegerField(max_length=100)),
                ('image', models.ImageField(null=True, upload_to='image')),
            ],
        ),
    ]
