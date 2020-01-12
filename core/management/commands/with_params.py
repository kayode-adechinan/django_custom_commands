from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "fake data generator"

    def add_arguments(self, parser):
        # Required argument
        parser.add_argument('total', type=int, help='Indicates the number of item to be created')

        # Optional argument
        parser.add_argument('-p', '--price', type=str, help='Define an item price', )

        # Optional list argument
        parser.add_argument('-i', '--items', nargs='+', type=int, help='Item ID')



    def handle(self, *args, **options):
        total = options['total']
        price = options['price']
        items = options['items']



        self.stdout.write(self.style.SUCCESS('total "%s"' % total))
        if price:
            self.stdout.write(self.style.SUCCESS('price "%s"' % price))
        if items:
            self.stdout.write(self.style.SUCCESS('items "%s"' % items))