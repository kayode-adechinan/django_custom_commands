from django.core.management.base import BaseCommand
from core import models

class Command(BaseCommand):
    help = "fake data generator"

    def handle(self, *args, **options):
        # add any logic here : play with data, do anything !
        models.Item.objects.create(name="first item")

        self.stdout.write(self.style.SUCCESS("fixture successfully generated!"))