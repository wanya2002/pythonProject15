from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Student(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='имя')
    last_name = models.CharField(max_length=100, verbose_name='фамилия')
    avatar = models.ImageField(upload_to='students/', verbose_name='аватар', **NULLABLE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'студент'
        verbose_name_plural = 'студенты'
        ordering = ('last_name',)

class Breed(models.Model):
    name = models.CharField(max_length=50, verbose_name='порода', help_text='укажите породу')
    descrition = models.TextField(verbose_name='описание породы', help_text='введите описание', **NULLABLE)

    class Meta:
        verbose_name = 'порода'
        verbose_name_plural = 'породы'

    def __str__(self):
        return self.name



class Dog(models.Model):
    name = models.CharField(max_length=50, verbose_name='кличка', help_text='введите кличку собаки')
    breed = models.ForeignKey(Breed, on_delete=models.SET_NULL, verbose_name='порода',
                              help_text='введите породу собаки', **NULLABLE, related_name='dogs',)
    photo = models.ImageField(upload_to='catalog/photo', verbose_name='фото', help_text='установите фото', **NULLABLE)
    data_birth = models.DateField(verbose_name='дата рождения', help_text='birth', **NULLABLE)

    class Meta:
        verbose_name = 'собака'
        verbose_name_plural = 'собаки'
        ordering = ['name', 'breed']

    def __str__(self):
        return f'{self.name} - {self.breed}'


