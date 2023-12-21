from django.core.management.base import BaseCommand
import random

from django.db import transaction

from datatables.models import Datatable
from tqdm import tqdm

# python manage.py seed --mode=refresh

""" Clear all data and creates addresses """
MODE_REFRESH = 'refresh'

""" Clear all data and do not create any object """
MODE_CLEAR = 'clear'


class Command(BaseCommand):
    help = "seed database for testing and development."

    def add_arguments(self, parser):
        parser.add_argument('--mode', type=str, help="Mode")

    def handle(self, *args, **options):
        self.stdout.write('seeding data...')
        run_seed(self, options['mode'])
        self.stdout.write('done.')


def clear_data():
    """Deletes all the table data"""
    print("Delete Address instances")
    Datatable.objects.all().delete()


def create_datatables():
    """Creates an address object combining different elements from the list"""
    names = ["ALexey", "Andrew", "Stepan", "Yury", "Evgeniy"]
    codes = ["PHP", "Ruby", "Go", "Python", "C", "C++", "C#", "JavaScript", "HTML", "SQL"]
    descriptions = [str(i) for i in range(1000000, 9999999, 100000)]
    urls = ["http://github.com/", "http://msn.com/", "http://abw.by/", "http://google.com/", "http://vk.ru/"]
    costs = [str(i) for i in range(100, 1000, 5)]

    return Datatable(
        name=random.choice(names),
        code=random.choice(codes),
        description=random.choice(descriptions),
        url=random.choice(urls),
        cost=random.choice(costs),
    ).save()


def run_seed(self, mode):
    """ Seed database based on mode

    :param mode: refresh / clear
    :return:
    """
    # Clear data from tables
    clear_data()
    if mode == MODE_CLEAR:
        return

    for i in tqdm(range(10000)):
        create_datatables()

