# Generated by Django 3.2.8 on 2021-11-04 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('q7', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alvo',
            name='expiration_date',
            field=models.DateField(),
        ),
    ]