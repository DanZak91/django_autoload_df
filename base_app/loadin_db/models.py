from django.db import models

# Create your models here.


class Employ(models.Model):
    """Занятость города"""

    city = models.CharField(max_length=50, verbose_name="Город")  # Город
    surface_type = models.CharField(max_length=100, verbose_name="Тип поверхности")  # Тип поверхности
    osv = models.CharField(max_length=3, verbose_name="Осв")  # Осв
    side = models.CharField(max_length=5, verbose_name="Сторона")  # Сторона
    address = models.CharField(max_length=200, verbose_name="Адрес")  # Адрес
    vn_code = models.CharField(max_length=30, verbose_name="Вн.код")  # Вн.код
    latitude = models.FloatField(verbose_name="Широта")  # Широта
    longitude = models.FloatField(verbose_name="Долгота")  # Долгота
    photo_diagram = models.URLField(verbose_name="Фото/Схема")  # Фото/Схема
    price_with_vat = models.FloatField(null=True, verbose_name="Прайс c НДС")  # Прайс C НДС
    count_impressions = models.FloatField(null=True, default=0, verbose_name="Диджтал кол-во показов")  # Дидж кол-во показов
    grp = models.FloatField(null=True, verbose_name="GRP")  # GRP
    ots = models.FloatField(null=True, verbose_name="OTS")  # OTS
    code_espar = models.CharField(max_length=30, null=True, verbose_name="КодЭспар")  # КодЭспар
    july2023 = models.TextField(null=True, verbose_name="Июль 2023")
    august2023 = models.TextField(null=True, verbose_name="Август 2023")
    september2023 = models.TextField(null=True, verbose_name="Сентябрь 2023")
    october2023 = models.TextField(null=True, verbose_name="Октябрь 2023")
    november2023 = models.TextField(null=True, verbose_name="Ноябрь 2023")
    december2023 = models.TextField(null=True, verbose_name="Декабрь 2023")
    material = models.TextField(null=True, verbose_name="Материал носителя")  # Материал носителя
    product_restriction = models.TextField(null=True, verbose_name="Ограничения по продукту")  # Ограничения по продукту
    city_district = models.CharField(max_length=50, null=True, verbose_name="Городской округ")  # Городской округ
    tech_requirements = models.URLField(null=True, verbose_name="Технические требования")  # Технические требования
    mounting_price_with_vat = models.FloatField(null=True, verbose_name="Монтаж. Прайс  с НДС")  # Монтаж. Прайс  с НДС
    regluing_price_with_vat = models.FloatField(null=True,
                                                verbose_name="Переклейка. Прайс с НДС")  # Переклейка. Прайс с НДС
    resolution_po = models.CharField(null=True, max_length=10, verbose_name="Разрешение ПО")  # Разрешение ПО
    note = models.TextField(null=True)   # Примечание
