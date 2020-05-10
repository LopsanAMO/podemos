# Generated by Django 3.0.6 on 2020-05-10 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentCalendar',
            fields=[
                ('id', models.IntegerField(default=97111770891, editable=False, primary_key=True, serialize=False)),
                ('num_payment', models.IntegerField(db_column='num_pago')),
                ('amount', models.DecimalField(db_column='monto', decimal_places=2, max_digits=15)),
                ('payment_date', models.DateField(db_column='fecha_pago')),
                ('status', models.CharField(choices=[('PEN', 'PENDIENTE'), ('PAG', 'PAGADO'), ('PAR', 'PARCIAL'), ('ATR', 'ATRASADO')], db_column='estatus', max_length=15)),
                ('account', models.ForeignKey(db_column='cuenta_id', on_delete=django.db.models.deletion.CASCADE, to='accounts.Account')),
            ],
            options={
                'db_table': 'CalendarioPagos',
            },
        ),
    ]
