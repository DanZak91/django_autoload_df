import os
import pandas as pd
import openpyxl
from django.core.management.base import BaseCommand

from loadin_db.models import Employ

file = '\Занятость города 2023.xlsx'
path = "\\".join(str(os.path.dirname(os.path.realpath(__file__))).split(os.sep)[:-4]) + file

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)


class Command(BaseCommand):
    help = 'Автозагрузка датасета в БД'

    def add_argument(self):
        pass

    def handle(self, *args, **options):
        df = pd.DataFrame(pd.read_excel(path, sheet_name="Статус", usecols=lambda x: 'Unnamed' not in x, skipfooter=10))
        col_hyp = openpyxl.load_workbook(path)
        col_hyp_sheets = col_hyp['Статус']
        links = []
        for i in range(2, len(col_hyp_sheets['K']) - 9):
            links.append(col_hyp_sheets.cell(row=i, column=11).hyperlink.target)
        df['фото/схема'] = links

        cou = 0

        # МЕТОД №1

        # for i in df.values:
        #     data = Employ.objects.create(
        #         city=i[0], surface_type=i[1], osv=i[2], side=i[3],
        #         address=i[4], vn_code=i[5], latitude=i[6], longitude=i[7],
        #         photo_diagram=i[8], price_with_vat=i[9], count_impressions=i[10], grp=i[11],
        #         ots=i[12], code_espar=i[13], july2023=i[14], august2023=i[15],
        #         september2023=i[16], october2023=i[17], november2023=i[18], december2023=i[19],
        #         material=i[20], product_restriction=i[21], city_district=i[22], tech_requirements=i[23],
        #         mounting_price_with_vat=i[24], regluing_price_with_vat=i[25], resolution_po=i[26], note=i[27]
        #     ).save()
        #     cou += 1
        #     print(f'ROW = {cou}')
        # print(f'Выполнено успешно ! Добавлено строк = {cou}')


        # МЕТОД №2 - МАССОВАЯ ВСТАВКА ДАННЫХ. СОКРАЩАЕТ ВРЕМЯ МИНИМУМ в 2х и более раз
        bulk_list = []
        for i in df.values:
            data = Employ(
                city=i[0], surface_type=i[1], osv=i[2], side=i[3],
                address=i[4], vn_code=i[5], latitude=i[6], longitude=i[7],
                photo_diagram=i[8], price_with_vat=i[9], count_impressions=i[10], grp=i[11],
                ots=i[12], code_espar=i[13], july2023=i[14], august2023=i[15],
                september2023=i[16], october2023=i[17], november2023=i[18], december2023=i[19],
                material=i[20], product_restriction=i[21], city_district=i[22], tech_requirements=i[23],
                mounting_price_with_vat=i[24], regluing_price_with_vat=i[25], resolution_po=i[26], note=i[27]
            )
            cou += 1
            print(f'ROW = {cou}')
            bulk_list.append(data)
        Employ.objects.bulk_create(bulk_list)
        print(f'Выполнено успешно ! Добавлено строк = {cou}')

        # МЕТОД № 3
        # Загрузка файла через Админку.