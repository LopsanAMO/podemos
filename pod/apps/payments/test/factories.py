import factory
import random
import datetime
from factory.fuzzy import FuzzyDate, FuzzyDecimal
from pod.apps.accounts.test.factories import AccountFactory
from pod.apps.payments.models import PaymentCalendar


class PaymentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'payments.PaymentCalendar'

    id = random.randrange(200, 99999)
    account = factory.SubFactory(AccountFactory)
    num_payment = random.randrange(1,4)
    amount = FuzzyDecimal(0.5,9999.9)
    balance = FuzzyDecimal(0.5,9999.9)
    payment_date = FuzzyDate(datetime.datetime.now())
    status = factory.Faker(
        'random_element', elements=[x[1] for x in PaymentCalendar.STATUS]
    )
