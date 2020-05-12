# Generated by Django 3.0.6 on 2020-05-11 05:52

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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_payment', models.IntegerField(db_column='num_pago')),
                ('amount', models.DecimalField(db_column='monto', decimal_places=2, max_digits=15)),
                ('payment_date', models.DateField(db_column='fecha_pago')),
                ('status', models.CharField(choices=[('pen', 'PENDIENTE'), ('pag', 'PAGADO'), ('par', 'PARCIAL'), ('atr', 'ATRASADO')], db_column='estatus', default='pen', max_length=15)),
                ('account', models.ForeignKey(db_column='cuenta_id', on_delete=django.db.models.deletion.CASCADE, to='accounts.Account')),
            ],
            options={
                'db_table': 'CalendarioPagos',
            },
        ),
    ]
