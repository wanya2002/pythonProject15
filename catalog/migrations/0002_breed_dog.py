# Generated by Django 3.2.25 on 2025-03-06 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='укажите породу', max_length=50, verbose_name='порода')),
                ('descrition', models.TextField(blank=True, help_text='введите описание', null=True, verbose_name='описание породы')),
            ],
            options={
                'verbose_name': 'порода',
                'verbose_name_plural': 'породы',
            },
        ),
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='введите кличку собаки', max_length=50, verbose_name='кличка')),
                ('photo', models.ImageField(blank=True, help_text='установите фото', null=True, upload_to='catalog/photo', verbose_name='фото')),
                ('data_birth', models.DateField(blank=True, help_text='birth', null=True, verbose_name='дата рождения')),
                ('breed', models.ForeignKey(blank=True, help_text='введите породу собаки', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dogs', to='catalog.breed', verbose_name='порода')),
            ],
            options={
                'verbose_name': 'собака',
                'verbose_name_plural': 'собаки',
                'ordering': ['name', 'breed'],
            },
        ),
    ]
