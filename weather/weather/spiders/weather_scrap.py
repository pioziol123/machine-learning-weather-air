# -*- coding: utf-8 -*-
import scrapy
import pandas as pd
import datetime
import numpy as np


class WeatherScrapSpider(scrapy.Spider):
    name = 'weather-scrap'
    allowed_domains = ['weather.com']
    start_urls = ['https://weather.com/pl-PL/pogoda/dzisiaj/l/210036ee3963854e507c1fdb804560b821aa8c0a25661de14efccf0c87f7f8c0']
    file_path = ''
    def parse(self, response):
        temp = response.xpath("//div[@class='today_nowcard-temp']/span").re('>(\d+)<')[0]
        df = pd.DataFrame([[temp, datetime.datetime.now().date().isoformat()]], columns=['Temperatura', 'Data'])
        pd.read_csv(self.file_path, index_col=0).merge(df, how='outer').to_csv(self.file_path)
        pass
