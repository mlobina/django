import csv

from django.core.management.base import BaseCommand
from phones.models import Phone
from django.utils.text import slugify


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:

            phone_reader = csv.reader(csvfile, delimiter=';')
            # пропускаем заголовок
            next(phone_reader)

            for phone_id, name, image, price, release_date, lte_exists, _ in phone_reader:
                # TODO: Добавьте сохранение модели
                p = Phone(id=phone_id,
                          name=name,
                          image=image,
                          price=price,
                          release_date=release_date,
                          lte_exists=lte_exists,
                          slug=slugify(name, allow_unicode=True)
                          )
                p.save()


