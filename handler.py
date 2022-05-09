import json
import requests
import datetime
import time
from database import Database

class Handler():
    def __init__(self, api_key):
        self.key = api_key
        self.year = ''
        self.month = ''
        self.day = ''
        self._stock_profile = {}
        self.db = Database()
        
    def get_stock_profile(self):
        self.create_stock_profile()
        for i in self._stock_profile:
            self.update_stock(i)
        return self._stock_profile
        
    def create_stock_profile(self):
        self.db.update()
        stocks_targets = self.db.get_stock_db()
        for i in stocks_targets:
            self._stock_profile[i] = [stocks_targets[i],0,0,0,0]
            #(target price, day low price, day high price, day open price, day close price)
            
    def update_date(self):
        self.year = str(datetime.date.today().year)
       
        month = datetime.date.today().month
        if month < 10:
            self.month = '0' + str(month)
        else:
            self.month = str(month)
        
        day = datetime.date.today().day - 1
        if day < 10: 
            self.day = '0' + str(day)
        else:
            self.day = str(day)
            
    def add_stock(self, name, target):
        target = str(target)
        name = name.upper()
        if len(self._stock_profile) < 5:
            self.db.add_stock_name_target(name,target)
        else:
            print("\nYou already have 5 stocks!")
    
    def remove_stock(self, name):
        name = name.upper()
        self.db.remove_stock(name)
            
    def update_stock(self, stock_name):
        url = f'https://api.polygon.io/v1/open-close/{stock_name}/{self.year}-{self.month}-{self.day}?adjusted=true&apiKey={self.key}'
        print(url)
        try:
            stock_info = requests.get(url).json()
            self._stock_profile[stock_name][1] = stock_info['low']
            self._stock_profile[stock_name][2] = stock_info['high']
            self._stock_profile[stock_name][3] = stock_info['open']
            self._stock_profile[stock_name][4] = stock_info['close']
        except:
            print("Please wait one minute and try again. Maximum requests per minute exceeded!")
            
    
    def clear_stock(self):
        self.db.clear_database()