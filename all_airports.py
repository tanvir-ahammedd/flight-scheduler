import csv
from Airport import Airport

class AllAirports:
    def __init__(self):
        self.airports = None
        
        self.load_airpoart_data('./data/airport.csv')
        
    
    def load_airpoart_data(self, file_path):
        airports = {}
        currency_rates = {}
        country_currency = {}
        
        #curency name <---> rate
        with open('./data/currencyrates.csv', 'r') as file:
            lines = csv.reader(file)
                
            for line in lines:
                currency_rates[line[1]] = line[2]
        file.close()
        
        #country <---> currency
        with open('./data/countrycurrency.csv', 'r') as file:
            lines = csv.reader(file)

            for line in lines:
                country_currency[line[0]] = line[1]
        file.close()
        
        #create airport
        with open(file_path, 'r', encoding='utf8') as file:
            lines = csv.reader(file)
            try:
                for line in lines:
                    country = line[3]
                    currency = country_currency[country]
                    rate = currency_rates[currency]
                    airports[line[4]] = Airport(line[4], line[1], line[2], line[3], line[6], line[7], 0)
            except KeyError as e:
                print(e)

        self.airports = airports
        for airport in airports.items():
            print(airport)
            
AllAirports()
