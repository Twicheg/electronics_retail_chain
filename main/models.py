from django.db import models


class ChainLink(models.Model):
    companies = (("factory", "Завод"), ("retail", "Розничная сеть"), ("individual", "Индивидуальный предприниматель"))

    title = models.CharField(max_length=100, verbose_name="название")
    email = models.EmailField(max_length=100, verbose_name='контактный е-мейл')
    country = models.CharField(max_length=10, verbose_name="страна")
    city = models.CharField(max_length=20, verbose_name='город')
    street = models.CharField(max_length=20, verbose_name="улица")
    house_number = models.IntegerField(verbose_name="номер дома")
    product_name = models.CharField(max_length=100, verbose_name="название продукта")
    product_model = models.CharField(max_length=10, verbose_name="модель продукта")
    exit_date = models.DateField(verbose_name="дата выхода продукта")
    provider = models.ForeignKey("main.ChainLink", null=True, blank=True, verbose_name="поставщик",
                                 on_delete=models.CASCADE)
    debt = models.FloatField(verbose_name="задолженность перед поставщиком")
    creation = models.DateTimeField(auto_created=True, auto_now=True, verbose_name="время создания")
    company = models.CharField(default="factory", choices=companies)
    relationship_level = models.IntegerField(default=0, verbose_name="уровень отношений")

    def __str__(self):
        return f'{self.title},{self.provider},{self.debt}'

    class Meta:
        verbose_name = "звено сети"
        verbose_name_plural = "звенья сети"
