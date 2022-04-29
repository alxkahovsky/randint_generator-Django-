from django.core.management.base import BaseCommand
from randint_generator.models import RandomInt
import random
import time


class Command(BaseCommand):
    def handle(self, *args, **options):
        i = 0
        t_time = 60
        i_time = 0
        while True:
            start_time = time.time()
            random_ints = RandomInt.objects.all()
            if random_ints:
                random_int = random_ints[0]
                random_int.random_number = random.randint(0, 9999999)
                random_int.save()
            else:
                RandomInt.objects.create(random_number=random.randint(0, 9999999))
                continue
            i = i + 1
            end_time = time.time()
            time.sleep(5 - (end_time - start_time))
            i_time = i_time + (5 - (time.time() - start_time))
            if i == 12 or i_time > t_time:
                break
