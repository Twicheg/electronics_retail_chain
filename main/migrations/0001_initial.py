# Generated by Django 5.0.1 on 2024-01-06 12:06

import django.db.models.deletion
import main.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChainLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation', models.DateTimeField(auto_created=True, verbose_name='время создания')),
                ('title', models.CharField(max_length=100, verbose_name='название')),
                ('email', models.EmailField(max_length=100, verbose_name='контактный е-мейл')),
                ('country', models.CharField(max_length=10, verbose_name='страна')),
                ('city', models.CharField(max_length=20, verbose_name='город')),
                ('street', models.CharField(max_length=20, verbose_name='улица')),
                ('house_number', models.IntegerField(verbose_name='номер дома')),
                ('product_name', models.CharField(max_length=100, verbose_name='название продукта')),
                ('product_model', models.CharField(max_length=10, verbose_name='модель продукта')),
                ('exit_date', models.DateField(verbose_name='дата выхода продукта')),
                ('debt', models.FloatField(validators=[main.validators.validate_debt], verbose_name='задолженность перед поставщиком')),
                ('relationship_level', models.IntegerField(default=0, verbose_name='уровень отношений')),
                ('provider', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='main.chainlink', verbose_name='поставщик')),
            ],
        ),
    ]