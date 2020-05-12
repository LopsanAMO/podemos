import factory
import random
import pytz
import datetime
from factory.fuzzy import FuzzyDateTime, FuzzyDecimal
from pod.apps.accounts.test.factories import AccountFactory


class TransactionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'transactions.Transaction'

    id = random.randrange(200, 99999)
    account = factory.SubFactory(AccountFactory)
    date = FuzzyDateTime(datetime.datetime.utcnow().replace(tzinfo=pytz.utc))
    amount = FuzzyDecimal(0.5, 9999.9)