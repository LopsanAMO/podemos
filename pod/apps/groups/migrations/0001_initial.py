# Generated by Django 3.0.6 on 2020-05-11 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.CharField(default='DBEC1', editable=False, max_length=5, primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='nombre', max_length=20)),
            ],
            options={
                'db_table': 'Grupos',
            },
        ),
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'Miembros',
            },
        ),
    ]
