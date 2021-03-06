# Generated by Django 3.2.8 on 2021-11-04 02:49

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_cargo', models.CharField(max_length=200, unique=True, verbose_name='Cargo')),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome')),
                ('admissao', models.DateField(default=datetime.date.today, verbose_name='Data de Admissao')),
                ('id_cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pessoa', to='q1.cargo')),
            ],
        ),
    ]
