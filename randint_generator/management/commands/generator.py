from django.core.management.base import BaseCommand
from randint_generator.models import RandomInt
import time
import random

class Command(BaseCommand):
    while 1 == 1:
        time.sleep(5)
        random_ints = RandomInt.objects.all()
        if random_ints:
            random_int = random_ints[0]
            random_int.random_number = random.randint(0, 9999999)
            random_int.save()
        else:
            RandomInt.objects.create(random_number=random.randint(0, 9999999))
            continue
