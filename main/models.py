from django.db import models

from main.validators import validate_debt


class ChainLink(models.Model):
    title = models.CharField(max_length=100, verbose_name="название")
    email = models.EmailField(max_length=100, verbose_name='контактный е-мейл')
    country = models.CharField(max_length=10, verbose_name="страна")
    city = models.CharField(max_length=20, verbose_name='город')
    street = models.CharField(max_length=20, verbose_name="улица")
    house_number = models.IntegerField(verbose_name="номер дома")
    product_name = models.CharField(max_length=100, verbose_name="название продукта")
    product_model = models.CharField(max_length=10, verbose_name="модель продукта")
    exit_date = models.DateField(verbose_name="дата выхода продукта")
    provider = models.ForeignKey("main.ChainLink", default=0, verbose_name="поставщик", on_delete=models.CASCADE)
    debt = models.FloatField(verbose_name="задолженность перед поставщиком", validators=[validate_debt])
    creation = models.DateTimeField(auto_created=True, verbose_name="время создания")
    relationship_level = models.IntegerField(default=0, verbose_name="уровень отношений")
