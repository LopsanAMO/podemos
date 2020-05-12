import os
import csv
from enum import Enum
from django.core.management.base import BaseCommand
from django.test import override_settings
from unipath import Path
from pod.apps.users.models import Client
from pod.apps.accounts.models import Account
from pod.apps.groups.models import Members, Group
from pod.apps.transactions.models import Transaction
from pod.apps.payments.models import PaymentCalendar

ROOT_DIR = Path(__file__).ancestor(6)


class Tables(Enum):
    calendariopagos = (PaymentCalendar, )
    clientes = (Client, )
    cuentas = (Account, )
    grupos = (Group, )
    miembros = (Members, )
    transacciones = (Transaction, )

    @classmethod
    def get_value(cls, val):
        try:
            return cls[val].value[0]
        except KeyError:
            return False


class Command(BaseCommand):
    def get_files(self):
        _files = []
        for root, dirs, files in os.walk(str(ROOT_DIR) + '/data/'):
            self.stdout.write(self.style.SUCCESS(os.path.basename(root)))
            for f in files:
                _files.append('{}/data/{}{}'.format(ROOT_DIR,os.path.basename(root), f))
        return _files

    @override_settings(SIGNALS=False)
    def handle(self, *args, **options):
        _list = ['clientes', 'grupos', 'miembros', 'cuentas', 'transacciones', 'calendariopagos']
        files = self.get_files()
        file_counter = 0
        valid = True
        while valid:
            element = _list[file_counter]
            for i in range(len(files)):
                file = files[i]
                if element in file:
                    model = file.replace(str(ROOT_DIR), '').replace('/data/data_', '').replace('.csv', '')
                    model = Tables.get_value(model)
                    line_count = 0
                    with open(file) as f:
                        csv_reader = csv.reader(f, delimiter=',')
                        for row in csv_reader:
                            if line_count == 0:
                                pass
                            else:
                                print(row)
                                model.create(*row)
                            line_count += 1
                    files.remove(file)
                    file_counter += 1
                    break
            if file_counter == 6:
                valid = False
        self.stdout.write(self.style.SUCCESS('Data filled Successfully :D'))