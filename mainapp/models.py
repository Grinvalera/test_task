from django.db import models

Category_cars = [
    ('Mazda', 'Mazda'),
    ('Bmw', 'Bmw'),
    ('Audi', 'Audi')
]


class Car(models.Model):

    brand_car = models.CharField(max_length=64, choices=Category_cars, verbose_name='Марка автомобиля')
    model_car = models.CharField(max_length=128, verbose_name='Модель автомобиля')
    title_car = models.TextField(verbose_name='Об автомобиле')
    price_car = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена автомобиля')
    image_car = models.ImageField(verbose_name='Фото автомобиля')

    def __str__(self):
        return "{} - {}".format(self.brand_car, self.model_car)


class News(models.Model):

    heading_news = models.CharField(max_length=128, verbose_name='Заголовок')
    title_news = models.TextField(verbose_name='Текст новости')
    create_news = models.DateTimeField(verbose_name='Дата добавления новости')

    def __str__(self):
        return "{} - {}".format(self.heading_news, self.create_news)


class Contact(models.Model):

    phone = models.CharField(max_length=64, verbose_name='Номер телефона')
    address = models.CharField(max_length=128, verbose_name='Адресс автосалона')
    e_mail = models.EmailField(max_length=256, verbose_name='Почта')

# Create your models here.
