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
            name='Transaction',
            fields=[
                ('id', models.IntegerField(default=28111886150, editable=False, primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True, db_column='fecha')),
                ('amount', models.DecimalField(db_column='monto', decimal_places=2, max_digits=15)),
                ('account', models.ForeignKey(db_column='cuenta_id', on_delete=django.db.models.deletion.CASCADE, to='accounts.Account')),
            ],
            options={
                'db_table': 'Transacciones',
            },
        ),
    ]
