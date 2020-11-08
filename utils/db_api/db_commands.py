from asgiref.sync import sync_to_async

from wg_djangopanel.telegrambot.usermanage.models import User, Order


@sync_to_async
def add_user(user_id, full_name, username):
    try:
        return User(user_id=int(user_id), name=full_name, username=username).save()
    except Exception:
        return select_user(int(user_id))


# Вывод всех пользователей
@sync_to_async
def select_all_users():
    users = User.objects.all()
    return users


# Выбор одного пользователья
@sync_to_async
def select_user(user_id: int):
    user = User.objects.filter(user_id=user_id).first()
    return user


# Считает сколько пользователей
@sync_to_async
def count_users():
    total = User.objects.all().count()
    return total

@sync_to_async
def update_user_tel(id: int, tel):
    customer = User.objects.filter(user_id=id).first()
    customer.tel=tel
    customer.save()
    return customer

@sync_to_async
def add_order(customer_id: int, date, time, type, amount, typeofevent):
    order = Order(customer_id=customer_id,date=date,time=time,type=type,amount=amount,typeofevent=typeofevent).save()
    return order
