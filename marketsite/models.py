from django.db import models


class Orders(models.Model):
    name = models.CharField("І'мя", max_length=200)
    tel = models.CharField("Телефон", max_length=200)
    add_info = models.TextField("Додаткова інформація")
    count = models.PositiveIntegerField("Кількість")
    delivery = models.CharField("Спосіб доставки", max_length=10)
    size = models.CharField("Розмір", max_length=1)
    pub_date = models.DateTimeField("Дата")

    def __str__(self):
        return self.name

