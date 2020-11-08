from django.db import models


class TimedBaseModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Создание таблицы (наследует от TimedBaseModel) Пользователь, при нажатие кнопки старт записывается в эту таблицу
class User(TimedBaseModel):
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    id = models.AutoField(primary_key=True)
    user_id = models.BigIntegerField(verbose_name="ID Users Telegram", unique=True, default=1)
    name = models.CharField(verbose_name="Full name of user", max_length=100)
    username = models.CharField(verbose_name="Username Telegram", max_length=100, null=True)
    tel = models.CharField(verbose_name="tel", max_length=100, null=True)

    def __str__(self):
        return f"№{self.id} ({self.user_id}) - {self.name}"

class Order(TimedBaseModel):
    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    id = models.AutoField(primary_key=True)
    customer_id = models.BigIntegerField(verbose_name="id of customer", default=1)
    date = models.CharField(verbose_name="Date of order",max_length=50)
    time = models.CharField(verbose_name="Time of order", max_length=50)
    type = models.CharField(verbose_name="Type of order", max_length=100)
    amount = models.CharField(verbose_name="Amount", max_length=100)
    typeofevent = models.CharField(verbose_name="Typeofevent ", max_length=100)

