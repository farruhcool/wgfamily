from django.contrib import admin

from wg_djangopanel.telegrambot.usermanage.models import User, Order


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "user_id", "name", "username", "tel")


# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "customer_id", "date", "time", "type", "amount", "typeofevent")
