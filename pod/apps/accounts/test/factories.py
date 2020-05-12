import factory
from factory.fuzzy import FuzzyDecimal, FuzzyInteger
from pod.apps.groups.test.factories import GroupFactory
from pod.apps.accounts.models import Account


class AccountFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Account

    id = factory.Sequence(lambda n: f'A{n}')
    group = factory.SubFactory(GroupFactory)
    status = factory.Faker(
        'random_element', elements=Account.STATUS.list()
    )
    amount = FuzzyDecimal(0.5,9999.9)
    balance = FuzzyDecimal(0.5,9999.9)
    num_payments = FuzzyInteger(1, 8)

