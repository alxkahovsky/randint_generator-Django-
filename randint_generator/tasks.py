from background_task import background
from .models import RandomInt
import random


@background(schedule=5)
def notify_user(user_id):
    number = random.randint(0, 9999999)
    rand_int = RandomInt.objects.all()
    if rand_int:
        rand_int.random_number = number
        rand_int.save()
    else:
        RandomInt.objects.create(number)
